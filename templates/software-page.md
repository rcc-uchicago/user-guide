<!--
Software page template for the RCC User Guide.

How to use:
1. Copy this file to docs/software/apps-and-envs/<name>.md
2. Replace every <PLACEHOLDER> and delete sections or tabs that do not apply
3. Add the page to the "Commonly Used" list in mkdocs.yml and to docs/software/index.md
4. Run `mkdocs serve` locally to check tabs, admonitions, and links

Conventions:
- Show real `module avail` / `module show` output copied from the cluster
- Use `pi-[cnetid]` for accounts and `[your-cnetid]` for user names
- Every job script must include --account, --partition, and --time
- Use /scratch/midway3/$USER (not /scratch/$USER) on Midway3
- Delete this comment block before publishing
-->

# <SOFTWARE NAME>

[<SOFTWARE NAME>](<https://official-website-or-github>) is <one or two sentences: what it does and who uses it>.

Keywords: `<field>`, `<field>`, `<method>`, `<method>`

## Available modules

You can check the available <SOFTWARE NAME> modules via `module avail <module-name>`:

=== "Midway2"
    ```
    ---------------------------- /software/modulefiles2 ----------------------------
    <module-name>/<version>  <module-name>/<version>(default)
    ```

===+ "Midway3"
    ```
    ---------------------------- /software/modulefiles -----------------------------
    <module-name>/<version>  <module-name>/<version>(default)
    ```

You can show the dependencies and environment variables set by a module with `module show`. For example, on Midway3:

```
module show <module-name>/<version>
```

which gives

```
<paste the module show output>
```

<One sentence on what the output means, e.g., which compiler/MPI/CUDA it was built with and whether it should run on GPU nodes. Explain any module suffixes such as `-gpu` or `+multi`.>

## Example job scripts

An example batch script to run <SOFTWARE NAME> on Midway3 is given below:

```bash
#!/bin/bash
#SBATCH --job-name=<name>
#SBATCH --account=pi-[cnetid]
#SBATCH --partition=caslake
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=<N>
#SBATCH --cpus-per-task=<N>
#SBATCH --mem=<N>G

module load <module-name>/<version>

cd $SLURM_SUBMIT_DIR

<command to run, e.g., mpirun -np $SLURM_NTASKS <binary> -in input.txt>
```

where `<input file>` is <what the user needs to provide>.

<Optional: a second script for GPU nodes (partition=gpu, --gres=gpu:N, --constraint=<gpu type>), multi-node runs, or interactive use with sinteractive.>

## Build from source

<Include this section only if users may need a newer version or custom features. Otherwise, delete it.>

Since <SOFTWARE NAME> is under active development, you may want to build it from source to get the latest features and bug fixes. Below is an example using <toolchain> on Midway3:

```
module load <compiler> <mpi> <libraries> cmake/<version>
git clone <repository-url>
cd <repo>
git checkout <stable-tag>
<configure and build commands>
```

<Explain any non-obvious options, e.g., GPU architecture flags.>

## Getting help

- Official documentation: [<SOFTWARE NAME> documentation](<https://link>)
- Built-in help: `<command> --help` or `module help <module-name>/<version>`
- RCC support: [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target='_blank'}
- AI assistants: an AI assistant such as Claude can help you interpret errors and adapt the job scripts on this page. See [Getting help with AI assistants](../index.md#getting-help-with-ai-assistants) for what to include in your question and what not to share.
