
# Job arrays

Slurm job arrays provide a convenient way to submit a large number of
independent processing jobs. For example, Slurm job arrays can be
useful for applying the same or similar computation to a collection of
data sets. When a job array script is submitted, a specified number of
“array tasks” are created based on the “master” sbatch script.

Consider the following example (from `array.sbatch`):

```bash
#!/bin/bash

#SBATCH --job-name=array
#SBATCH --output=array_%A_%a.out
#SBATCH --error=array_%A_%a.err
#SBATCH --array=1-16
#SBATCH --time=01:00:00
#SBATCH --partition=broadwl
#SBATCH --ntasks=1
#SBATCH --mem=4G

# Print the task id.
echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID

# Add lines here to run your computations.
```

In this simple example, `--array=1-16` requests 16 array tasks
(numbered 1 through 16). The “array tasks” are copies of the master
script that are automatically submitted to the scheduler on your
behalf. In each array task, the environment variable
`SLURM_ARRAY_TASK_ID` is set to a unique value (in this
example, numbers ranging from 1 to 16).

Job array indices can be specified in several different ways. Here are
some examples:

```default
# A job array with array tasks numbered from 0 to 31.
#SBATCH --array=0-31

# A job array with array tasks numbered 1, 2, 5, 19, 27.
#SBATCH --array=1,2,5,19,27

# A job array with array tasks numbered 1, 3, 5 and 7.
#SBATCH --array=1-7:2
```

In the example sbatch script above, the `%A_%a` notation is filled
in with the master job id (`%A`) and the array task id (`%a`).
This is a simple way to create output files in which the file name is
different for each job in the array.

The remaining options in the sbatch script are the same as the options used in other, non-array settings; in this example, we are requesting
that each array task be allocated 1 CPU (`--ntasks=1`) and 4
GB of memory (`--mem=4G`) on the broadwl partition
(`--partition=broadwl`) for up to one hour
(`--time=01:00:00`).

Most partitions have limits on the number of array tasks that can run
simultaneously. To achieve a higher throughput, consider
[Parallel batch jobs](../srun-parallel/index.md#parallel-batch).

For more information about Slurm job arrays, consule the  the

```
`Slurm
documentation on job arrays`_
```
