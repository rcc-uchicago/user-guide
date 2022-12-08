# Job Arrays

According to the [Slurm Job Array Documentation](http://slurm.schedmd.com/job_array.html), “job arrays offer a mechanism for submitting and managing collections of similar jobs quickly and easily.” In general, job arrays are useful for applying the same processing routine to a collection of multiple input data files. Job arrays offer a very simple way to submit a large number of independent processing jobs.

By submitting a single job array sbatch script, a specified number of “array-tasks” will be created based on this “master” sbatch script. An example job array script is given below **array.sbatch**:

```bash 
#!/bin/bash

#SBATCH --job-name=arrayJob
#SBATCH --output=arrayJob_%A_%a.out
#SBATCH --error=arrayJob_%A_%a.err
#SBATCH --array=1-16
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000


######################
# Begin work section #
######################

# Print this sub-job's task ID
echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID

# Do some work based on the SLURM_ARRAY_TASK_ID
# For example: 
# ./my_process $SLURM_ARRAY_TASK_ID
# 
# where my_process is you executable
```

In the above example, The **--array=1-16** option will cause 16 array-tasks (numbered 1, 2, ..., 16) to be spawned when this master job script is submitted. The “array-tasks” are simply copies of this master script that are automatically submitted to the scheduler on your behalf. However, in each array-tasks an environment variable called **SLURM_ARRAY_TASK_ID** will be set to a unique value (in this example, a number in the range 1, 2, ..., 16). In your script, you can use this value to select, for example, a specific data file that each array-tasks will be responsible for processing.

Job array indices can be specified in a number of ways. For example:

```bash 
#A job array with index values between 0 and 31:
#SBATCH --array=0-31

#A job array with index values of 1, 2, 5, 19, 27:
#SBATCH --array=1,2,5,19,27

#A job array with index values between 1 and 7 with a step size of 2 (i.e. 1, 3, 5, 7):
#SBATCH --array=1-7:2
```

The **%A_%a** construct in the output and error file names is used to generate unique output and error files based on the master job ID (**%A**) and the array-tasks ID (**%a**). In this fashion, each array-tasks will be able to write to its own output and error file.

The remaining **#SBATCH** options are used to configure each array-tasks. All of the standard **#SBATCH** options are available here. In the **array.sbatch** example, we are requesting that each array-task be allocated 1 CPU core (**--ntasks=1**) and 4 GB (4000 MB) of memory (**--mem-per-cpu=4000**) in the sandyb partition (**--partition=sandyb**), and be allowed to run for up to 1 hour (**--time=01:00:00**). To be clear, the overall collection of 16 array-tasks will be allowed to take more than 1 hour to complete, but we have specified that each individual array-task will run for no more than 1 hour.

The total number of array-tasks that are allowed to run in parallel will be governed by the QoS of the partition to which you are submitting. In most cases, this will limit users to a maximum of 64 concurrently running array-tasks. To achieve a higher throughput of array-tasks, see [Parallel Batch Jobs](parallel.md)

More information about Slurm job arrays can be found in the [Slurm Job Array Documentation](http://slurm.schedmd.com/job_array.html).