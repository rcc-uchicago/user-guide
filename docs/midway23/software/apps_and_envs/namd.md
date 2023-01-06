# [NAMD](http://www.ks.uiuc.edu/Research/namd/)

`namd.sbatch` is a submission script that can be used to submit
the `apoa1.namd` calculation job to the queue.

```bash
#!/bin/sh

#SBATCH --job-name=namd
#SBATCH --output=namd-%j.out
#SBATCH --constraint=ib
#SBATCH --exclusive
#SBATCH --nodes=4

module load namd/2.9

mpirun namd2 apoa1.namd
```

The script can be submitted with this command:

```default
sbatch namd.sbatch
```
