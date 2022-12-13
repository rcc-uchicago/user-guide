# GAMESS

`gamess.sbatch` demonstrates how to submit a GAMESS job to Midway. In this example, we are going to use 4 nodes from the sandyb partition exclusively for a total of 64 cores across 4 nodes.  An example input deck is here: `example.inp`

```bash
#!/bin/bash

#SBATCH --output=gamess_example.out
#SBATCH --time=00:10:00
#SBATCH --partition=sandyb
#SBATCH --nodes=4
#SBATCH --exclusive
#SBATCH --constraint=ib

module load gamess

rungms example.inp $SLURM_NTASKS $SLURM_CPUS_ON_NODE 
```

You can submit to the queue with this command:

```default
sbatch gamess.sbatch
```
