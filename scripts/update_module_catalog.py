#!/usr/bin/env python3
"""Regenerate docs/software/module_catalog_<cluster>.tsv from a cluster's modulefiles.

Run this on the cluster (it needs read access to the modulefile tree), then
commit the updated TSV. The "Software Module Catalog" page is rendered from the TSV at
build time by hooks/module_catalog.py, so no access to /software is needed
when the docs are built.

    python3 scripts/update_module_catalog.py --cluster midway3
    python3 scripts/update_module_catalog.py --cluster midway2 --modulepath /software/modulefiles

PyYAML is used if available; otherwise a simple line-based parser reads the
.yaml files (enough for the name/description/tags/url fields used here).

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

try:
    import yaml
except ImportError:  # e.g. an older system Python without PyYAML
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_TEMPLATE = os.path.join(HERE, "..", "docs", "software", "module_catalog_{}.tsv")
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
    """Fallback for .yaml files that are not valid YAML (or when PyYAML is missing).

    Reads top-level `key: value` lines; any following line that is not a new
    top-level key is treated as a continuation of the previous value.
    """
    raw = {}
    key = None
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):(?:\s+(.*)|$)", line)
        if m:
            key = m.group(1)
            raw[key] = [(m.group(2) or "").strip()]
        elif key is not None and line.strip() and not line.lstrip().startswith("#"):
            raw[key].append(line.strip())
    data = {}
    for key, parts in raw.items():
        first = parts[0]
        if first in ("|", "|-", "|+", ">", ">-", ">+"):
            parts = parts[1:]
        items = [p for p in parts[1:] if p]
        if not first and items and all(p.startswith("- ") or p == "-" for p in items):
            data[key] = [p[1:].strip().strip("'\"") for p in items]  # block sequence
            continue
        value = " ".join(p for p in parts if p).strip()
        if value.startswith("["):
            end = value.find("]")
            value = value[1:end if end >= 0 else len(value)]
            data[key] = [v.strip().strip("'\"") for v in value.split(",")]
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
    if yaml is not None:
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
    p.add_argument("--cluster", required=True, help="cluster name, e.g. midway3 or midway2")
    p.add_argument("-o", "--output", help="default: docs/software/module_catalog_<cluster>.tsv")
    args = p.parse_args()
    args.cluster = args.cluster.lower()
    args.output = args.output or OUTPUT_TEMPLATE.format(args.cluster)

    entries = collect(args.modulepath)
    today = datetime.date.today().isoformat()
    with open(args.output, "w") as f:
        f.write(f"# Generated by scripts/update_module_catalog.py from {args.cluster}:{args.modulepath} on {today}\n")
        f.write("# Do not edit by hand; rerun the script on the cluster and commit the result.\n")
        f.write("#" + "\t".join(COLUMNS) + "\n")
        for e in entries:
            f.write("\t".join(e[c].replace("\t", " ") for c in COLUMNS) + "\n")

    untagged = sum(1 for e in entries if not e["tags"])
    print(f"Wrote {len(entries)} modules ({untagged} without tags) to {os.path.normpath(args.output)}")


if __name__ == "__main__":
    main()
