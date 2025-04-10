# `scode` Command-Line Tool – API Reference

This document provides a full API reference for `scode`, a command-line tool to manage and deploy VS Code Server environments on HPC clusters. This is intended for advanced users who want to understand all available subcommands, arguments, and behaviors.

---

## Command Overview

```bash
scode <command> [subcommand] [options]
```

---

## Global Architecture

- All VSCode environments and installations are managed under `~/.scode`.
- `scode` use SLURM (`sbatch`, `squeue`, `scancel`) to launch and manage VS Code Server jobs internally.
- Extensions are stored in environments under `~/.scode/envs`. A `default` environment is created automatically when running commands that requires an active environment.

---

## Commands and Arguments

### `serve-web` / `serve`

Launch a web-based VSCode server using SLURM.

```bash
scode serve-web [--version <version>] [--env <env>] -- <sbatch args>
```

**Arguments:**

- `--version`: Specific VSCode version to launch (default: `latest`)
- `--env`: Environment name to activate or create (default: `default`)
- `--`: Passes all remaining args directly to `sbatch`

**Example:**

```bash
scode serve-web --version latest --env default -- --account rcc --time 01:00:00 --partition caslake
```

---

### `jobs`

Manage and inspect running server jobs.

#### `jobs list`

List active jobs:
```bash
scode jobs list
```

#### `jobs status <job_id>`

Show detailed status and SSH tunnel instructions for a specific job:
```bash
scode jobs status 30317404
```

---

### `create`

Create a new environment.

```bash
scode create <env_name>
```

A `default` environment is created automatically when running commands that require an active environment.

---

### `list` / `ls` / `l`

List environments.

```bash
scode list
```

---

### `activate`

Activate a named environment.

```bash
scode activate <env_name>
```

---

### `remove` / `rm` / `uninstall`

Remove a named environment.

```bash
scode remove <env_name>
```

---

### `ext`

Manage extensions.

#### `ext install`

Install extensions by ID or from file.
```bash
scode ext install <extension_id>... [--env <env>]
scode ext install --file/-f extensions.txt [--env <env>]
```

#### `ext list`

List installed extensions.
```bash
scode ext list [--env <env>]
```

#### `ext update`

Update all extensions.
```bash
scode ext update [--env <env>]
```

#### `ext uninstall`

Remove one or more extensions.
```bash
scode ext uninstall <extension_id>... [--env <env>]
```

---

### `download`

Manage VSCode versions. The `download` command is primarily designed for system administrators to download and cache VSCode tarballs.

Users can also use this command to download specific versions of the VSCode Server for troubleshooting. Set the `SCODE_ARCHIVE_DIR` environment variable to specify a local directory for downloads.

```bash
scode download [options] [version]
```

**Options:**

- `--target/-t [cli|web]`: Download CLI or Web version (defaults to both)
- `--list/-l`: List available versions from upstream
- `--latest/-n N`: Download latest N releases
- `--versions/-v`: List locally downloaded versions
- `--cleanup/-c`: Remove corrupt or incomplete downloads

**Examples:**

```bash
scode download --list
scode download --latest 1
scode download 1.80.0 --target web
```
