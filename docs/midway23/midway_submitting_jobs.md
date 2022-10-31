# Submitting Jobs
The information here describes how users can submit jobs to compute nodes on Midway 2 or Midway 3 using either batch jobs or interactive jobs.

The following graphic shows the workflow for submitting jobs on Midway.
![Jobs Overview](img/running_jobs/jobs_overview.png)

## Batch Jobs

The `sbatch` command is used to request computing resources on the Midway clusters. Rather than specify all the options in the command line, users typically write an “sbatch script” that contains all the commands and parameters neccessary to run a program on the cluster.

### SBATCH Options

In an sbatch script, all Slurm parameters are declared with `#SBATCH`, followed by additional definitions.

Here is an example of a Midway 2 sbatch script:

```
#!/bin/bash
#SBATCH --job-name=example_sbatch
#SBATCH --output=example_sbatch.out
#SBATCH --error=example_sbatch.err
#SBATCH --time=00:05:00
#SBATCH --partition=broadwl
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=14
#SBATCH --mem-per-cpu=2000

module load openmpi
mpirun ./hello-mpi
```

And here is an explanation of what each of these options does:


|  <div style="width:200px">Option</div>      | Description |
| ----------- | ----------- |
| `--job-name=example_sbatch`      | Assigns name `example_sbatch` to the job.       |
| `--output=example_sbatch.out`   | Writes console output to file `example_sbatch.out`.        |
| `--error=example_sbatch.err`   | Writes error messages to file `example_sbatch.err`.        |
| `--time=00:05:00`   | Reserves the computing resources for 5 minutes (or less if program completes before 5 min).  | 
| `--partition=broadwl`   | Requests compute nodes from the broadwell partition on the Midway2 cluster. |
| `--nodes=4`   | Requests 4 compute nodes |
| `--ntasks-per-node=14`   | Requests 14 cores (CPUs) per node, for a total of 14 * 4 = 56 cores. |
| `--mem-per-cpu=2000`   | Requests 2000 MB (2 GB) of memory (RAM) per core, for a total of 2 * 14 = 28 GB per node. |


In this example, we have requested 4 compute nodes with 14 CPUs each. Therefore, we have requested a total of 56 CPUs for running our program. The last two lines of the script load the OpenMPI module and launch the MPI-based executable that we have called `hello-mpi`.

### Submitting a Batch Job

Continuing the example above, suppose that the sbatch script is saved in the current directory into a file called example.sbatch. This script is submitted to the cluster using the following command:
```
sbatch ./example.sbatch
```
or more generally:
```
sbatch ./<your_sbatch_file>
```

### Example Submission Scripts

Here are some example sbatch job submission scripts that demonstrate  the different options and jobs types you make wish to use.

**A single core job to the standard compute partition:**

=== "Midway2"

    ```
    #!/bin/bash
    
    #SBATCH --job-name=single-node-cpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=broadwl
    #SBATCH --ntasks-per-node=1  # number of tasks
    #SBATCH --cpus-per-task=1    # number of threads per task

    # LOAD MODULES
    module load python

    # DO COMPUTE WORK
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    python hello.py
    ```

=== "Midway3"

    ```
    #!/bin/sh

    #SBATCH --job-name=single-node-cpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=caslake
    #SBATCH --ntasks-per-node=1  # number of tasks
    #SBATCH --cpus-per-task=1    # number of threads per task

    # LOAD MODULES
    module load python

    # DO COMPUTE WORK
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    python hello.py
    ```

**A single node gpu job to the gpu partition:**

=== "Midway2"

    ```
    #!/bin/bash

    #SBATCH --job-name=1gpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=gpu2
    #SBATCH --gres=gpu:1
    #SBATCH --ntasks-per-node=1 # num cores to drive each gpu
    #SBATCH --cpus-per-task=1   # set this to the desired number of threads

    # LOAD MODULES
    module load tensorflow
    module load cudnn

    # DO COMPUTE WORK
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    python training.py
    ```

=== "Midway3"

    ```
    #!/bin/sh

    #SBATCH --job-name=1gpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=gpu
    #SBATCH --gres=gpu:1
    # TO USE V100 specify --constraint=v100
    # TO USE RTX600 specify --constraint=rtx6000
    #SBATCH --constraint=v100   # constraint job runs on V100 GPU use
    #SBATCH --ntasks-per-node=1 # num cores to drive each gpu
    #SBATCH --cpus-per-task=1   # set this to the desired number of threads

    # LOAD MODULES
    module load tensorflow
    module load cudnn

    # DO COMPUTE WORK
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    python training.py
    ```

**[Add another example here]**

You can find more example sbatch submission scripts in the [RCC SLURM workshop materials](https://github.com/rcc-uchicago/SLURM_WORKSHOP)

## Interactive Jobs
This section describes how to submit an “interactive job” on Midway 2 or Midway 3. This interactive session will persist until you disconnect from the compute node, or until you reach the maximum requested time.

To request an interactive job, run the following command:
```
sinteractive
```
As soon as the requested resources become available, sinteractive will do the following:
1. Log in to the node.
2. Change into the directory you were working in.
3. Set up X11 forwarding for displaying graphics.
4. Transfer your current shell environment, including any modules you have previously loaded.

By default, an interactive session times out after 2 hours. If you would like more than 2 hours, be sure to include a --time=HH:MM:SS flag to specify the necessary amount of time. For example, to request an interactive session for 6 hours, run the following command:

```
sinteractive --time=06:00:00
```

There are many additional options for the sinteractive command, including options to select the number of nodes, the number of cores per node, the amount of memory, and so on. For example, to request exclusive use of two compute nodes on the Midway broadwl partition for 8 hours, enter the following:
```
sinteractive --exclusive --partition=broadwl --nodes=2 --time=08:00:00
```
For more details about these and other useful options, read below about the sbatch command, and see Running jobs on midway. Note that all options available in the sbatch command are also available for the sinteractive command.

There is a debug QoS setup on the broadwl partition to help users quickly access some resources to debug or test their code before submitting their jobs to the main broadwl partition. The debug QoS will allow you to run one job and get up to 4 cores for 15 minutes. To use the debug QoS, you have to specify --time which should be 15 minutes or less. For example, to get 2 cores for 15 minutes, you could run:
```
sinteractive --qos=debug --time=00:15:00 --ntasks=2
```

An alternative to the sinteractive command is the srun command:
```
srun --pty bash
```
Unlike sinteractive, this command does not set up X11 forwarding, which means you cannot display graphics using srun. Both the srun and sinteractive commands have the same command options.