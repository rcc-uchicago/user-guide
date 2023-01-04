# [CP2K](http://www.cp2k.org)

`cp2k.sbatch` demonstrates how to run CP2K. `cp2k-H2O.tgz`
is a tarball with the H2O CP2K input deck used for this example.

```bash
#!/bin/sh

#SBATCH --output=cp2k-%j.out
#SBATCH --constraint=ib
#SBATCH --exclusive
#SBATCH --nodes=2

module load cp2k

mpirun cp2k.popt H2O-32.inp
```

You can submit to the queue with this command:

```default
sbatch cp2k.sbatch
```
