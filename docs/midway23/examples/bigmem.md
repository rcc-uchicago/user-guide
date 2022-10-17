# Large-memory jobs

The `bigmem2` partition is particularly well suited for computations
that need more than about 60 GB of memory; see [Types of Compute Nodes](../../using-midway/index.md#node-types) for
technical specifications of the bigmem2 nodes.

## Running a large-memory job

To submit a job to bigmem2, include this line in your sbatch script:

```bash
#SBATCH --partition=bigmem2
```

Additionally, it is important to use the `--mem` or
`--mem-per-cpu` options. For example, to request 8 CPU cores
and 128 GB of memory on a bigmem2 node, add the following to your
sbatch script:

```bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G
```

## Interactive computing on bigmem2

These same options can also be used to set up an sinteractive
session. For example, to access a bigmem2 node with 1 CPU
and 128 GB of memory, run:

```bash
sinteractive --partition=bigmem2 --ntasks=1 --cpus-per-task=8 --mem=128G
```
                            