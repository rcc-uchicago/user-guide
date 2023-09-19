# [NAMD](http://www.ks.uiuc.edu/Research/namd/)

[NAMD](http://www.ks.uiuc.edu/Research/namd/)  is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems.

Keywords: `biology`, `physics`, `chemistry`, `molecular dynamics`

## Available modules

There are several NAMD modules on Midway2 and Midway3 that you can check via `module avail namd`:

=== "Midway2"
    ```
    ---------------------------- /software/modulefiles2 ----------------------------
    namd/2.11+intelmpi-5.1+intel-16.0 
    namd/2.12+intelmpi-5.1+intel-16.0
    namd/2.13+intelmpi-5.1+intel-16.0
    namd/2.14+intelmpi-5.1+intel-16.0   

    ```
===+ "Midway3"
    ```
    ---------------------------- /software/modulefiles -----------------------------
    namd/2.14(default)
    namd/2.14+intel-2022.0
    namd/2.14+intel-2022.0+cuda-11.5
    namd/2.14+intel-2022.0+cuda-11.5+multi
    namd/2.14+intel-2022.0+multi
    ```
The `multi` suffix indicates that the module can run across multiple nodes. The `cuda-11.5` indicates that the module support GPU acceleration via CUDA. You can then show the dependency of individual modules, for example, on Midway3 if you do
```
module show namd/2.14+intel-2022.0+multi
```
you will get
```
-------------------------------------------------------------------
/software/modulefiles/namd/2.14+intel-2022.0+multi:

module-whatis   {setup namd 2.14 multiple-node compiled with intel-2022.0}
conflict        namd
module          load intelmpi/2021.5+intel-2022.0
prepend-path    PATH /software/namd-2.14-el8-x86_64+intel-2022.0/bin-multi
setenv          FI_PROVIDER mlx
setenv          NAMD_HOME /software/namd-2.14-el8-x86_64+intel-2022.0/bin-multi
setenv          CONV_RSH ssh
```

In this case you can see this module was compiled with `intelmpi/2021.5+intel-2022.0`. 

## Example job script

An example batch script to run NAMD for Midway3 is given as below
```
#!/bin/bash
#SBATCH --job-name="test-namd"
#SBATCH --account=pi-[cnetid]
#SBATCH -t 00:30:00
#SBATCH --partition=gpu
#SBATCH --nodes=2             # 2 nodes
#SBATCH --ntasks-per-node=1   # 1 process per node
#SBATCH --cpus-per-task=2     # 2 threads mapping to 2 cores per node (1 of them for inter-node comm)
#SBATCH --gres=gpu:2          # 2 GPUs per node
#SBATCH --constraint=v100

module load namd/2.14+intel-2022.0+cuda-11.5+multi

# calculate total processes (P) and procs per node (PPN)
PPN=$(( $SLURM_CPUS_PER_TASK * $SLURM_NTASKS_PER_NODE ))
P=$(( $PPN * $SLURM_NNODES ))

mpirun -np $P $NAMD_HOME/namd2 +ppn $PPN +devices 0,1 apoa1.namd

```

<!---
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
--->