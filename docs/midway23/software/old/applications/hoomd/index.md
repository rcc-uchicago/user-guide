# [HOOMD](http://codeblue.umich.edu/hoomd-blue/)

For full performance HOOMD should be run on GPUs. It can be run on
a CPU only but performance will not be comparable.

`hoomd.sbatch` demonstrates how to run the `polymer_bmark.hoomd` and
`lj_liquid_bmark.hoomd` on a GPU device.

```bash
#!/bin/sh

#SBATCH --time=0:10:00
#SBATCH --job-name=hoomd
#SBATCH --output=hoomd-%j.out
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

module load hoomd 

hoomd polymer_bmark.hoomd
hoomd lj_liquid_bmark.hoomd
```

The script can be submitted with this command:

```default
sbatch hoomd.sbatch
```
