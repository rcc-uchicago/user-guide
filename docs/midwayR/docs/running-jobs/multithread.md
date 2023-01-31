# Multi-thread jobs
This section describes how to request resources to run multi-threaded applications.

## Using tasks 
Requesting multiple threads for MKL libraries in python using the `--ntasks-per-node` 
flag. 

```bash 
#!/bin/bash
#SBATCH --job-name=test_sbatch
#SBATCH --output=test_sbatch.out
#SBATCH --error=test_sbatch.err
##SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#
# LOAD REQUIRED MODULES FOR JOB
module load  Anaconda3
#
# SET NUMBER OF THREADS
export OMP_NUM_THREADS=$SLURM_NTASKS_PER_NODE

# RUN JOB
python dotprod.py 
```