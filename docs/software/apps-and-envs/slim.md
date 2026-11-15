# SLiM

[SLiM](https://messerlab.org/slim/) (Selection on Linked Mutations) is a forward-time population genetic simulation framework developed by the Messer Lab. It uses the Eidos scripting language to define complex evolutionary scenarios including natural selection, demographic history, spatial structure, and quantitative traits. SLiM is widely used in evolutionary biology, population genetics, and ecological genetics research.

Keywords: `evolutionary biology`, `population genetics`, `forward simulation`, `Eidos`

## Available modules

SLiM is available in both a command-line interface (CLI) and a graphical interface (GUI). The examples on this page are based on Midway3, using `SLiM/5.2` (CLI) and `SLiM/5.2-gui` (GUI).

```
module avail SLiM
```

## Running SLiM on Midway3

Load the CLI module and verify the installation:

```bash
module load SLiM/5.2
slim -v
eidos -v
```

SLiM simulations are defined in `.slim` script files written in the Eidos language. A minimal neutral evolution example:

```slim
// neutral_drift.slim — Wright-Fisher neutral evolution
initialize() {
    initializeMutationRate(1e-7);
    initializeMutationType("m1", 0.5, "f", 0.0);
    initializeGenomicElementType("g1", m1, 1.0);
    initializeGenomicElement(g1, 0, 99999);
    initializeRecombinationRate(1e-8);
}
1 early() {
    sim.addSubpop("p1", 500);
}
10000 late() {
    sim.outputFull();
}
```

Run the script:

```bash
slim neutral_drift.slim
```

The Eidos interpreter (`eidos`) can also be used interactively or to run standalone Eidos scripts:

```bash
eidos my_script.eidosscript
```

### Batch job (Midway3)

Each SLiM simulation runs single-threaded. To run many independent replicate simulations in parallel, submit an array job:

```bash
#!/bin/bash
#SBATCH --job-name=slim-run
#SBATCH --account=pi-<cnetid>
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=02:00:00
#SBATCH --array=1-50
#SBATCH --output=slim_%A_%a.out

module load SLiM/5.2

slim -d REP=$SLURM_ARRAY_TASK_ID neutral_drift.slim
```

The `-d REP=$SLURM_ARRAY_TASK_ID` passes the replicate index as a constant into the script, which can be used to set the random seed or label output files:

```slim
initialize() {
    setSeed(REP);
    // ...
}
```

## Using SLiMgui on Midway3 (graphical interface)

SLiMgui provides a point-and-click environment for writing, running, and visualizing SLiM simulations. It requires a graphical desktop session and is only available on Midway3 via `SLiM/5.2-gui`.

1. Connect to Midway3 via [ThinLinc](../../connection/thinlinc/main.md).
2. Open a terminal in the ThinLinc desktop and start an interactive session on a compute node:
    ```bash
    sinteractive --account=pi-<cnetid> --partition=caslake --mem=8G --time=02:00:00
    ```
3. Load the GUI module and launch SLiMgui:
    ```bash
    module load SLiM/5.2-gui
    SLiMgui
    ```

