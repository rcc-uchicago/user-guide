# Batch Jobs

The `sbatch` command is the command most commonly used by RCC users to request computing resources on the Midway cluster. Rather than specify all the options in the command line, users typically write an “sbatch script” that contains all the commands and parameters neccessary to run a program on the cluster.

## SBATCH Options

In an sbatch script, all Slurm parameters are declared with `#SBATCH`, followed by additional definitions.

Here is an example of a Midway2 sbatch script:

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

## Submitting a Batch Job

Continuing the example above, suppose that the sbatch script is saved in the current directory into a file called example.sbatch. This script is submitted to the cluster using the following command:
```
sbatch ./example.sbatch
```
or more generally:
```
sbatch ./<your_sbatch_file>
```

## Example Submission Scripts

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