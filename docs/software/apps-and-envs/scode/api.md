# `scode` Command-Line Tool – API Reference

This document provides a full API reference for `scode`, a command-line tool to manage and deploy VSCode Server environments on HPC clusters. This is intended for advanced users who want to understand all available subcommands, arguments, and behaviors.

---

## Command Overview

```bash
scode <command> [subcommand] [options]
```

---

## Global Architecture

- All VSCode environments and installations are managed under `~/.scode`.
- `scode` uses SLURM (`sbatch`, `squeue`, `scancel`) to launch and manage VSCode Server jobs internally.
- Extensions are stored in environments under `~/.scode/envs`. A `default` environment is created automatically when running commands that requires an active environment.

---

## Commands and Arguments

### `serve-web` / `serve`

Launch a web-based VSCode Server using SLURM.

```bash
scode serve-web [--version <version>] [--env <env>] [--port <port>]
[--port-range <range>] [--setup-command <command>] [--setup-script <script>] [--sbatch-file <file>] -- [sbatch args]
```

**Arguments:**

- `--version`: Specific VSCode version to launch (default: `latest`)
- `--env`: Environment name to activate or create (default: `default`)
- `--port`: Port to bind the VSCode server. By default, `scode` will use a random port selected from the port range `49152-65535`. If both `--port` and `--port-range` are specified, `--port` will take precedence.
- `--port-range`: Specify a range of ports to use, for example, `--port-range 3000-3100` (default: `49152-65535`)
- `--setup-command`: Command to run before starting the VSCode server. This can be used to set up the environment, install dependencies, or perform any necessary pre-launch tasks. For example, `--setup-command "module load python/anaconda-2022.05"`.
- `--setup-script`: Path to a custom setup script to run before starting the VSCode server.
- `--sbatch-file`: Path to a custom SBATCH script file to use instead of the default. The SBATCH directives in this file will be used to configure the job submission, and the commands in the file will be executed before starting the VSCode server.
- `--`: All remaining arguments after the `--` separator are passed directly to `sbatch`

**Example:**

```bash
scode serve-web --version latest --env default -- --account rcc --time 01:00:00 --partition caslake
```

---

### `jobs`

Manage and inspect running server jobs.

#### `jobs list/ls/l`

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
scode ext install <extension_id>... [--env <env>] [--cli-version <version>] [--force]
scode ext install --file/-f extensions.txt [--env <env>] [--cli-version <version>] [--force]
```

#### `ext list/ls/l`

List installed extensions.
```bash
scode ext list [--env <env>] [--cli-version <version>]
```

#### `ext update`

Update all extensions.
```bash
scode ext update [--env <env>] [--cli-version <version>]
```

#### `ext uninstall/rm/remove`

Remove one or more extensions.
```bash
scode ext uninstall <extension_id>... [--env <env>] [--cli-version <version>]
```

**Notes:**

- Extensions are installed in the environment directory under `~/.scode/envs/<quality>/<env_name>/extensions`.
- If you are serving a non-latest version of VSCode by specifying `--version` with `scode serve-web`, you may need to specify a matching `--cli-version` when installing extensions to ensure compatibility.

---

### `download`

Manage VSCode versions. The `download` command is primarily designed for system administrators to download and cache VSCode tarballs.

Users can also use this command to download specific versions of the VSCode Server for troubleshooting. Set the `SCODE_ARCHIVE_DIR` environment variable to specify a local directory for downloads.

```bash
scode download [options] [version]
```

**Arguments:**

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
