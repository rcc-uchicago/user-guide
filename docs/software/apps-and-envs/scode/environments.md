# Managing `scode` Environments

This guide covers everything you need to create, switch between, and manage `scode` environments. These are lightweight, isolated workspaces stored in `~/.scode/envs/`, containing your VS Code Server extensions, user data, and cached assets.

---

## 1  What *is* an `scode` environment?

An **environment** is a directory at `~/.scode/envs/<quality>/<name>/` that contains:

- an `extensions/` folder for VS Code Server extensions
- a `data/` folder for user settings and server logs

You can think of it as the VS Code equivalent of a Conda environment: create as many as you like, each with its own extensions and settings.

In the environment path:

- `<quality>` is either `stable` or `insiders` (currently, `scode` only support the `stable` version of VS Code).
- `<name>` is the name for the scode environment, when you run a scode command that require a working `scode` environment (e.g., `scode serve` or `scode ext`), a default environment with the name `default` will be **automatically created and activated**.

The `default` environment should be sufficient for most use cases. Custom environments, however, can help isolate extension sets. They are ideal for troubleshooting conflicts or separating projects by programming languages.

---

## 2  Creating your first `scode` environment

```bash
# Create an custom `scode` env and have it activated globally
scode create myenv
scode activate myenv

# Install extensions into the activated environment
scode ext install ms-python.python ms-toolsai.jupyter

# Launch VS Code Server using that env
scode serve-web -- --account <pi-account> --time 01:00:00
```

1. `scode create <env_name>` initializes a new environment under `~/.scode/envs/stable/<env_name>/`.
2. `scode activate <env_name>` sets it as the global default (persisted in `~/.scode/env-stable`).
3. `scode ext install …` installs the specified extensions to the activated environment.
4. `scode serve-web` will launch the server with the extensions and user settings from the activated environment.

---

## 3  Command reference

### 3.1  `scode create`

- **Usage:** `scode create <env_name>`
- **Purpose:** Create a fresh `scode` environment.
- **Behavior:**

    - Directory `~/.scode/envs/stable/<env_name>/` is created (quality defaults to *stable*).
    - No VS Code binaries are installed yet. That happens lazily on first `serve-web`.
    - Errors out if `<env_name>` already exists.

### 3.2  `scode activate`

- **Usage:** `scode activate <env_name>`
- **Purpose:** Activate and use an `scode` env globally.
- **Behavior:**

    - A plaintext file `~/.scode/env-<quality>` stores the environment  selection.
    - Subsequent `scode` commands inherit this env **unless** an explicit `--env` overrides it.

### 3.3  `scode list`

- **Usage:** `scode list`
- **Output example:**

    ```bash
    Local stable channel environments:
       myenv
    *  default
    ```

    An asterick `*` indicates the currently active environment.

### 3.4  `scode remove`

- **Usage:** `scode remove <env_name>`
- **Purpose:** Removes an `scode` env with all associated extensions and user data
- **Behavior:**
    - Recursively deletes the env directory.
    - If an active environment is removed, the next available environment will be activated automatically.

---

## 4  Using environments with `serve-web`

Both of the following examples starts a VS Code server with the `myenv` `scode` environment.

1. **Inline**: pass `--env <name>` every time

    ```bash
    scode serve-web --env myenv -- --time 02:00:00 --account <pi-account>
    ```

2. **Activate**: permanently sets an environment as global default

    ```bash
    scode activate myenv
    scode serve-web -- --time 02:00:00 --account <pi-account>
    ```

!!! tip

    If you omit both `--env` *and* `activate`, `scode` falls back to the implicit **`default`** environment (created and activated on first use).

---

## 5  Extension compatibility

- **Isolation:** Extensions live under `~/.scode/envs/<quality>/<name>/extensions`. They never bleed into other envs.
- **Version coupling:** If you serve VS Code version `1.86.0` inside env *foo*, extensions compiled for that version roam with it.

*TODO: Write more about version mismatch here*

---

## 7  Troubleshooting environments

| Symptom                                        | Likely cause / fix                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| Extensions missing after upgrade               | They’re per‑env; re‑install in the new env                         |
| Disk quota exceeded in `$HOME`                 | Delete unused envs and old tarballs (see §6.3)                     |

*TODO: Write more about setting SCODE_HOME to free up home dir space*
