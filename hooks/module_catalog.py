"""MkDocs hook: render the Midway3 software module catalog.

Any page containing the marker  <!-- MODULE_CATALOG -->  gets it replaced by
tables of modules grouped by category, built from docs/software/module_catalog.tsv
(regenerate that file with scripts/update_module_catalog.py).

The yaml `tags:` of the modules are free-form, so CATEGORIES below maps the raw
tags onto a curated set of categories. A module is listed under every category
that one of its tags maps to; modules with no mapped tag go under "Other".
Unmapped tags are reported when running `mkdocs build -v`.
"""

import logging
import os
import re

log = logging.getLogger("mkdocs.hooks.module_catalog")

MARKER = "<!-- MODULE_CATALOG -->"
CATALOG = os.path.join("software", "module_catalog.tsv")  # relative to docs_dir
OTHER = "Other"

# Category -> raw tags (lowercase) that map onto it. Order = order on the page.
CATEGORIES = {
    "Biology & Bioinformatics": [
        "biology", "bioinformatics", "genomics", "genetics", "genomes", "metagenomics",
        "binning", "evolution", "protein", "proteins", "alphafold", "structure-prediction",
        "structural-biology",
    ],
    "Chemistry & Materials": [
        "chemistry", "materials", "materials science", "dft", "molecular modeling",
        "molecular structures", "molecular dynamics and many-body perturbation theory",
    ],
    "Molecular Dynamics": [
        "molecular dynamics", "generalized-ensemble simulation system",
    ],
    "Physics & Astronomy": [
        "physics", "high energy physics", "astrophysics", "quantum", "quantum science",
        "quantum computing", "photonic", "electronics simulation em",
    ],
    "Earth & Climate Science": [
        "climate", "atmosphere", "ocean", "land", "sea-ice", "glaciology", "geophysics",
        "earth-system-model", "cesm", "wrf", "waccm", "waccm-ma", "f19_g17", "f2000climo",
        "bw1850", "bwma1850",
    ],
    "GIS & Geospatial": [
        "geospatial", "gis", "satellite", "raster", "vector", "geocoding",
    ],
    "Engineering & Simulation": [
        "simulation", "multiphysics", "finite element", "fea", "cfd", "cad", "mesh",
        "geometry", "modeling",
    ],
    "Imaging & Microscopy": [
        "image processing", "image-processing", "image", "bioimaging", "microscopy",
        "smlm", "medical imaging", "neuroscience", "cryo-em", "cryo-et", "cryoet",
        "tomography", "particle-picking", "computer vision", "point-cloud",
    ],
    "Visualization & Graphics": [
        "visualization", "graphics", "plotting", "3d", "gui", "desktop-application",
    ],
    "AI & Machine Learning": [
        "ai", "machine-learning", "machine learning", "deep-learning", "llm", "inference",
        "vllm", "diffusion", "ai-agent", "agent", "mcp", "openai-api",
    ],
    "Mathematics & Statistics": [
        "statistics", "r", "mathematics", "math", "linear algebra", "numerical analysis",
        "fft", "optimization", "solver",
    ],
    "Data & Databases": [
        "data", "database", "rdbms", "data analysis", "data analytics", "data processing",
        "parquet", "tiledb", "array", "io", "compression", "linguistics",
    ],
    "Compilers & Languages": [
        "compilers", "oneapi", "programming", "general programming", "scientific programming",
        "python", "rust", "fortran", "coding", "assembler", "scientific",
    ],
    "Parallel Computing & GPU": [
        "mpi", "hpc", "high performance computing", "high-performance computing",
        "high performance computing cuda", "high performance computing cuda mpi",
        "parallel", "distributed", "gpu", "cuda", "nvidia", "communication",
        "checkpointing",
    ],
    "Development Tools & Libraries": [
        "development", "library", "build-tools", "build", "version control", "testing",
        "profiling", "tracing", "performance analysis", "memory check", "postmortem",
        "package-manager", "package management", "conda", "container", "reproducibility",
        "environment", "docs", "documentation", "reference", "typesetting", "text editor",
        "text processing", "text", "crypto", "security", "x86", "systems", "system",
        "command runner",
    ],
    "Data Transfer & Cloud": [
        "globus", "data-transfer", "data-sharing", "s3", "aws", "cloud", "cloud computing",
        "ftp client", "faas", "compute",
    ],
    "Cluster Utilities": [
        "slurm", "sbatch", "sacct", "job-failure", "scheduling", "monitoring", "telemetry",
        "quota", "du", "disk-usage", "inodes", "gpfs", "storage", "file", "file manager",
        "manager", "terminal", "tui", "cli", "utilities", "tools", "scripts", "scode",
        "wizard", "web browser",
    ],
    "Multimedia": [
        "video", "audio", "codec", "media", "av1", "jpeg-2000", "vif",
    ],
}

TAG_TO_CATEGORY = {tag: cat for cat, tags in CATEGORIES.items() for tag in tags}


def _read_catalog(path):
    header, modules = [], []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            if line.startswith("#"):
                header.append(line.lstrip("#").strip())
                continue
            cols = (line.split("\t") + [""] * 6)[:6]
            name, versions, default, tags, url, desc = (c.strip() for c in cols)
            modules.append({
                "name": name,
                "versions": [v for v in versions.split(";") if v],
                "default": default,
                "tags": [t for t in tags.split(";") if t],
                "url": url,
                "description": desc,
            })
    return header, modules


def _anchor(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _md_escape(text):
    return (text.replace("\\", "\\\\").replace("|", "\\|")
                .replace("<", "&lt;").replace(">", "&gt;")
                .replace("*", "\\*").replace("_", "\\_"))


def _row(m):
    name = f"`{m['name']}`"
    if m["url"].startswith(("http://", "https://")):
        name = f"[{name}]({m['url']}){{:target='_blank'}}"
    versions = ", ".join(
        f"**`{v}`** (default)" if v == m["default"] else f"`{v}`" for v in m["versions"]
    )
    desc = _md_escape(m["description"]) or "&nbsp;"
    return f"| {name} | {versions} | {desc} |"


def _render(modules):
    groups = {cat: [] for cat in list(CATEGORIES) + [OTHER]}
    unmapped = set()
    for m in modules:
        cats = []
        for t in m["tags"]:
            cat = TAG_TO_CATEGORY.get(t.lower())
            if cat is None:
                unmapped.add(t)
            elif cat not in cats:
                cats.append(cat)
        for cat in cats or [OTHER]:
            groups[cat].append(m)
    if unmapped:
        log.info("module catalog: tags not mapped to a category: %s", ", ".join(sorted(unmapped)))

    out = [f"There are **{len(modules)}** software modules on Midway3. "
           "A module may appear under more than one category.", ""]
    out.append(" &middot; ".join(f"[{cat}](#{_anchor(cat)}) ({len(ms)})"
                                  for cat, ms in groups.items() if ms))
    out.append("")
    for cat, ms in groups.items():
        if not ms:
            continue
        out += [f"## {cat} {{ #{_anchor(cat)} }}", "",
                "| Module | Versions | Description |",
                "| ------ | -------- | ----------- |"]
        out += [_row(m) for m in sorted(ms, key=lambda m: m["name"].lower())]
        out.append("")
    return "\n".join(out)


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown
    path = os.path.join(config["docs_dir"], CATALOG)
    try:
        header, modules = _read_catalog(path)
    except OSError as e:
        log.warning("module catalog: cannot read %s: %s", path, e)
        return markdown.replace(MARKER, "!!! warning\n    The module catalog is unavailable.\n")
    generated = next((h for h in header if h.startswith("Generated")), "")
    m = re.search(r"on (\d{4}-\d{2}-\d{2})", generated)
    if m:
        markdown = markdown.replace("<!-- MODULE_CATALOG_DATE -->", m.group(1))
    return markdown.replace(MARKER, _render(modules))
