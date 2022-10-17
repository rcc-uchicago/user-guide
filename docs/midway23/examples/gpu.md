# GPU jobs

The `gpu2` partition is dedicated to software that uses Graphical
Processing Units (GPUs). See [Types of Compute Nodes](../../using-midway/index.md#node-types) for technical
specifications of the gpu2 nodes.

CUDA and OpenACC are two widely used tools for developing GPU-based
software. For information on compiling code with CUDA and OpenACC, see
[CUDA and OpenACC Compilers](../../software/compilers/nvidia/index.md#gpu-compiling).

## Running GPU code on Midway2

To submit a job to one of the GPU nodes, you must include the
following lines in your sbatch script:

```bash
#SBATCH --partition=gpu2
#SBATCH --gres=gpu:N
```

where `N` is the number of GPUs  requested. Allowable settings for `N` range from 1 to 4. If your application is entirely GPU
driven, then you do not need to explicilty request cores as one
CPU core will be assigned by default to act as a master to launch
the GPU based calculation. If however your application is mixed
CPU-GPU then you will need to request the number of cores with –ntasks
as is required by your job.

Here is an example sbatch script that allocates GPU resources and loads
the CUDA compilers (see also `gpu.sbatch`):

```bash
#!/bin/bash

#SBATCH --job-name=gpu   # job name
#SBATCH --output=gpu.out # output log file
#SBATCH --error=gpu.err  # error file
#SBATCH --time=01:00:00  # 1 hour of wall time
#SBATCH --nodes=1        # 1 GPU node
#SBATCH --partition=gpu2 # GPU2 partition
#SBATCH --ntasks=1       # 1 CPU core to drive GPU
#SBATCH --gres=gpu:1     # Request 1 GPU

# Load all required modules below. As an example we load cuda/9.1
module load cuda/9.1

# Add lines here to run your GPU-based computations.

```
