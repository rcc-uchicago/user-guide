#!/usr/bin/env python3
"""Regenerate docs/software/module_catalog.tsv from the Midway3 modulefiles.

Run this on Midway3 (it needs read access to the modulefile tree), then commit
the updated TSV. The "Software Module Catalog" page is rendered from the TSV at
build time by hooks/module_catalog.py, so no access to /software is needed
when the docs are built.

    python3 scripts/update_module_catalog.py
    python3 scripts/update_module_catalog.py --modulepath /software/modulefiles -o docs/software/module_catalog.tsv

For every module (top-level directory under --modulepath) the script collects:
  * the versions, i.e. what `module avail` shows: every file below the module
    directory that starts with the "#%Module" magic cookie
  * the default version from .version (if present)
  * description and url from the .yaml next to the default (or newest) version
  * the union of the `tags:` from all versions' .yaml files

Output format: one module per line, tab-separated, sorted by name:
    module  versions  default  tags  url  description
versions and tags are separated by ";". Lines starting with "#" are comments.
"""

import argparse
import datetime
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT = os.path.join(HERE, "..", "docs", "software", "module_catalog.tsv")
COLUMNS = ["module", "versions", "default", "tags", "url", "description"]


def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def is_modulefile(path):
    try:
        with open(path, "rb") as f:
            return f.read(8) == b"#%Module"
    except OSError:
        return False


def find_versions(moddir):
    """Return module versions (paths relative to moddir), like `module avail`."""
    versions = []
    for root, dirs, files in os.walk(moddir, followlinks=True):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            if fname.startswith(".") or fname.endswith((".yaml", ".yml", "~")):
                continue
            path = os.path.join(root, fname)
            if is_modulefile(path):
                versions.append(os.path.relpath(path, moddir))
    return sorted(versions, key=natural_key)


def read_default(moddir):
    path = os.path.join(moddir, ".version")
    try:
        with open(path) as f:
            m = re.search(r'ModulesVersion\s+"?([^"\s]+)"?', f.read())
            return m.group(1) if m else ""
    except OSError:
        return ""


def read_hidden(moddir, name):
    """Return (whole module hidden, set of hidden versions) from .modulerc."""
    hidden_all, hidden = False, set()
    try:
        with open(os.path.join(moddir, ".modulerc")) as f:
            lines = f.readlines()
    except OSError:
        return hidden_all, hidden
    for line in lines:
        words = line.split()
        if not words or words[0] != "module-hide":
            continue
        for w in words[1:]:
            if w.startswith("-"):
                continue
            if w == name:
                hidden_all = True
            elif w.startswith(name + "/"):
                hidden.add(w[len(name) + 1:])
    return hidden_all, hidden


def parse_lenient(text):
    """Fallback for .yaml files that are not valid YAML: read `key: value` lines."""
    data = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            data[key] = [v.strip().strip("'\"") for v in value[1:-1].split(",")]
        else:
            data[key] = value.strip("'\"")
    return data


def load_yaml(path):
    try:
        with open(path, errors="replace") as f:
            text = f.read()
    except OSError as e:
        print(f"warning: cannot read {path}: {e}", file=sys.stderr)
        return {}
    try:
        data = yaml.safe_load(text)
        if isinstance(data, dict):
            return data
    except yaml.YAMLError:
        pass
    return parse_lenient(text)


def as_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        value = value.split(",")
    if not isinstance(value, (list, tuple)):
        value = [value]
    return [str(v).strip() for v in value if v is not None and str(v).strip()]


def clean(text):
    """Collapse whitespace so a value fits on one TSV line."""
    if text is None:
        return ""
    return " ".join(str(text).split())


def collect(modulepath):
    entries = []
    for name in sorted(os.listdir(modulepath), key=natural_key):
        moddir = os.path.join(modulepath, name)
        if name.startswith(".") or not os.path.isdir(moddir):
            continue
        hidden_all, hidden = read_hidden(moddir, name)
        if hidden_all:
            continue
        versions = [v for v in find_versions(moddir) if v not in hidden]
        if not versions:
            continue
        default = read_default(moddir)
        if default not in versions:
            default = ""

        metas = {}
        for v in versions:
            for ext in (".yaml", ".yml"):
                ypath = os.path.join(moddir, v + ext)
                if os.path.isfile(ypath):
                    metas[v] = load_yaml(ypath)
                    break

        # Prefer metadata of the default version, then the newest version.
        order = ([default] if default else []) + list(reversed(versions))
        description = url = ""
        for v in order:
            meta = metas.get(v, {})
            description = description or clean(meta.get("description"))
            url = url or clean(meta.get("url"))

        tags = []
        seen = set()
        for v in order:
            for tag in as_list(metas.get(v, {}).get("tags")):
                tag = clean(tag).lower()
                if tag and tag not in seen:
                    seen.add(tag)
                    tags.append(tag)

        entries.append({
            "module": name,
            "versions": ";".join(versions),
            "default": default,
            "tags": ";".join(t.replace(";", ",") for t in tags),
            "url": url,
            "description": description,
        })
    return entries


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--modulepath", default="/software/modulefiles")
    p.add_argument("-o", "--output", default=DEFAULT_OUTPUT)
    args = p.parse_args()

    entries = collect(args.modulepath)
    today = datetime.date.today().isoformat()
    with open(args.output, "w") as f:
        f.write(f"# Generated by scripts/update_module_catalog.py from {args.modulepath} on {today}\n")
        f.write("# Do not edit by hand; rerun the script on Midway3 and commit the result.\n")
        f.write("#" + "\t".join(COLUMNS) + "\n")
        for e in entries:
            f.write("\t".join(e[c].replace("\t", " ") for c in COLUMNS) + "\n")

    untagged = sum(1 for e in entries if not e["tags"])
    print(f"Wrote {len(entries)} modules ({untagged} without tags) to {os.path.normpath(args.output)}")


if __name__ == "__main__":
    main()
