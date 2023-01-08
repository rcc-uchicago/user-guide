# Illustrative examples

Below are a number of example submission scripts that you can adapt to
run your jobs on Midway. See also the materials from the
[RCC Slurm workshop](https://github.com/rcc-uchicago/SLURM_WORKSHOP)
for additional examples.

The [SLURM](https://slurm.schedmd.com/documentation.html)  documentation
is always a good reference for all the `#SBATCH` parameters below.

## Simple Jobs

A typical batch script for simple jobs is given below

=== "Midway2"
    ```
    #!/bin/bash

    #SBATCH --job-name=single-node-cpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=broadwl  # accessible partitions listed by the sinfo command
    #SBATCH --ntasks-per-node=1  # number of tasks per node
    #SBATCH --cpus-per-task=1    # number of CPU cores per task

    # Load the require module(s)
    module load python

    # match the no. of threads with the no. of CPU cores
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK  

    # Load the require module(s)
    python analyze.py
    ```
===+ "Midway3"
    ```
    #!/bin/bash

    #SBATCH --job-name=single-node-cpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=caslake  # accessible partitions listed by the sinfo command
    #SBATCH --ntasks-per-node=1  # number of tasks per node
    #SBATCH --cpus-per-task=1    # number of CPU cores per task

    # Load the require module(s)
    module load python

    # match the no. of threads with the no. of CPU cores
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK  

    # Load the require module(s)
    python analyze.py
    ```

???+ note
    * If your application supports multithreading (e.g. with OpenMP), you want to specify the number of CPU cores per task greater than 1, e.g. `#SBATCH --cpus-per-task=8`
    * You can check the available partitions to your account via the command `rcchelp sinfo` to specify in `--partition`.
    * You can concatenate more than one runs in a job script.
    * If the job submission fails, please read the error message carefully: there are information regarding invalid combinations of `partition`, `account` or `qos` that may help you correct.

### Large-Memory Jobs

If your calculaltions need more than about 60 GB of memory, submit the job to the `bigmem2` partition on Midway2. You can query the technical specfication of the partition via
```
scontrol show partition bigmem2
```
and then `scontrol show node` to find out the memory capacity of its individual nodes.

To submit a job to `bigmem2`, include this line in your sbatch script:

```bash
#SBATCH --partition=bigmem2
```

Additionally, it is important to use the `--mem` or
`--mem-per-cpu` options. For example, to request 8 CPU cores
and 128 GB of memory on a bigmem2 node, add the following to your
sbatch script:

```bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G
```

These same options can also be used to set up an sinteractive session.
For example, to access a `bigmem2` node with 1 CPU and 128 GB of memory, run:

```bash
sinteractive --partition=bigmem2 --ntasks=1 --cpus-per-task=8 --mem=128G
```


## MPI Jobs

Many applications employ Message Passing Interface (MPI) for distributed and parallel computing to
improve performance. For more information on the MPI libraries available on Midway,
check with  `module avail openmpi` and `module avail intelmpi`. It is recommended to use the more recent modules to compile your codes (e.g. `intelmpi` 2021 and later, `openmpi` 3.0 and later).
<!--
see [Message Passing Interface (MPI)](../../software/libraries/mpi/index.md#mpi-libraries).
-->

Below is a simple C program (`test-mpi.c`) that you can use as a test for your MPI build and the loaded MPI libraries.

```c
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[], char *envp[]) {
  int numprocs, rank, namelen;
  char processor_name[MPI_MAX_PROCESSOR_NAME];

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Get_processor_name(processor_name, &namelen);

  printf("Process %d on %s out of %d\n", rank, processor_name, numprocs);

  MPI_Finalize();
}

```

Copy `test-mpi.c` to your home directory on Midway, load the
default OpenMPI module, and compile the program on a Midway login
node:

```default
module load openmpi
mpicc test-mpi.c -o mytest
```

???+ note
    It is recommended to check that the version of `mpicc` is the one you wanted via `which mpicc`.

Then prepare a job script `test.sbatch` to submit a job to Midway to run the program:

```bash
#!/bin/bash

#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
#SBATCH --partition=broadwl

# Load the default OpenMPI module that you used to compile the source file.
module load openmpi

# Run the MPI program with mpirun. Although the -n flag is not required and
# mpirun will automatically figure out the best configuration from the
# Slurm environment variables, it is recommended to specify -n and/or -ppn
# as explicit as possible.

n=$(( SLURM_NUM_NODES * SLURM_NTASKS_PER_NODE ))
mpirun -n $n --bind-to core --map-by core ./mytest

```

???+ note
    The options `--bind-to core --map-by core` added to the `mpirun` command
    indicates that the MPI tasks should be bound to physical CPU cores to improve performance.

Submit the MPI job to the Slurm job scheduler from a Midway login
node:

```default
sbatch test.sbatch
```

<!---
Here is an example output:

```default
Process 1 on midway2-0172.rcc.local out of 56
Process 3 on midway2-0172.rcc.local out of 56
Process 5 on midway2-0172.rcc.local out of 56
...
Process 50 on midway2-0174.rcc.local out of 56
Process 33 on midway2-0174.rcc.local out of 56
```

From this output, we observe that the computation is distributed on 4
different nodes, with many threads running simultaneously on the same
node.

When developing your own sbatch script for MPI-based computations,
keep in mind the following points.

Without the `--constraint=fdr` or `--constraint=edr`
options, your computations may run on nodes with FDR, EDR, or
combination of both.

It is possible to control the number of tasks that are run per node
with the `--ntasks-per-node` option. For example, submitting
the job like this to Midway:

```default
sbatch --ntasks-per-node=1 hellompi.sbatch
```

results in each thread running on a different node:

```default
Process 52 on midway2-0175.rcc.local out of 56 
Process 50 on midway2-0173.rcc.local out of 56
Process 49 on midway2-0172.rcc.local out of 56
...
Process 6 on midway2-0017.rcc.local out of 56
Process 21 on midway2-0096.rcc.local out of 56
Process 19 on midway2-0072.rcc.local out of 56
Process 23 on midway2-0100.rcc.local out of 56
```
--->

???+ note
    Both OpenMPI and IntelMPI have the ability to launch MPI programs
    directly with the Slurm command **srun**. It is not necessary to use this mode for most jobs, but it may provide additional job launch options. For example, from a Midway login node it is possible
    to launch the above `hellompi` program using OpenMPI using 28 MPI processes:

```default
srun -n28 hellompi
```

With IntelMPI, you need to also set an environment variable for this
to work:

```default
export I_MPI_PMI_LIBRARY=/software/slurm-current-$DISTARCH/lib/libpmi.so
srun -n28 hellompi
```

## Hybrid MPI/OpenMP Jobs

The following simple C source code (`test-hybrid.c`) illustrates
a hybrid MPI/OpenMP program that you can use to test.

```c
#include <stdio.h>
#include <omp.h>
#include "mpi.h"

int main(int argc, char *argv[]) {
  int numprocs, rank, namelen;
  char processor_name[MPI_MAX_PROCESSOR_NAME];
  int iam = 0, np = 1;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Get_processor_name(processor_name, &namelen);

  #pragma omp parallel default(shared) private(iam, np)
  {
    np = omp_get_num_threads();
    iam = omp_get_thread_num();
    printf("Hello from thread %d out of %d from process %d out of %d on %s\n",
           iam, np, rank, numprocs, processor_name);
  }

  MPI_Finalize();
}
```

To run the program on the RCC cluster, copy `test-hybrid.c` to your home directory,
then compile the code by entering the following commands into a terminal on a Midway2 login node:

```default
module load openmpi
mpicc -fopenmp test-hybrid.c -o mytest
```

Here we load the default OpenMPI compiler, but it should be possible to
use any available MPI compiler to compile and run this example. Note
that the option `-fopenmp` must be used here to compile the
program because the code includes OpenMP directives (use
`-openmp` for the Intel compiler and `-mp` for the PGI compiler).

Then prepare `test.sbatch` is a submission script that can be used
to submit a job to Midway2 to run the `mytest` program.

```bash
#!/bin/bash

# A job submission script for running a hybrid MPI/OpenMP job on
# Midway2.
             
#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=8
#SBATCH --partition=broadwl
#SBATCH --constraint=edr       # constraint for the inter-node MPI interface

# Load the default OpenMPI module.
module load openmpi

# Set OMP_NUM_THREADS to the number of CPUs per task we asked for.
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

mpirun ./hellohybrid
```

The options are similar to running an MPI job, with some differences:

* `--ntasks=2` specifies the number of MPI processes (or tasks).
* `--cpus-per-task=8` allocates 8 CPUs for each task.
* `export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK` sets the number of
OpenMP threads to the number of requested cores (CPUs) for each
task.

You can submit `test.sbatch` using the following
command from one of Midway2 login nodes:


```default
sbatch test.sbatch
```


## GPU Jobs

There are GPU nodes on both Midway2 and Midway3 where you can run GPU-enabled applications. You can check the partition `gpu2` (on `Midway2`) and `gpu` (on Midway3) to see their constituent nodes:
=== "Midway2"
    ```
    scontrol show partition gpu2
    ```
===+ "Midway3"
    ```
    scontrol show partition gpu
    ```
and then check the features of the individual nodes, for example,
=== "Midway2"
    ```
    scontrol show node midway2-gpu02
    ```
===+ "Midway3"
    ```
    scontrol show node midway3-0278
    ```
which shows NVIDIA Tesla V100 or Quadro RTX6000 GPUs.

To submit a job to one of the GPU nodes, you must specify the correct partition and the number of GPUs
in the batch scripts, for example for job scripts on Midway2:

```bash
#SBATCH --partition=gpu2
#SBATCH --gres=gpu:N
```
where `N` is the number of GPUs  requested. Allowable settings for `N` range from 1 to 4 depending on the number of GPUs per node.
<!--
If your application is entirely GPU driven, then you do not need to explicitly request cores as one
CPU core will be assigned by default to act as a master to launch the GPU based calculation.
If however your application is mixed CPU-GPU then you will need to request the number of cores with –ntasks
as is required by your job.
--->

=== "Midway2"

    ```
    #!/bin/bash

    #SBATCH --job-name=1gpu-example
    #SBATCH --account=pi-[group]
    #SBATCH --partition=gpu2
    #SBATCH --gres=gpu:1
    #SBATCH --ntasks-per-node=1 # num of tasker per node to drive the GPUs in the node
    #SBATCH --cpus-per-task=1   # set this to the desired number of threads

    # LOAD MODULES
    module load tensorflow
    module load cudnn

    # DO COMPUTE WORK
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    python training.py
    ```
===+ "Midway3"
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



Depending on the software packages you are using in the script,
their dependency would be the CUDA and OpenACC modules.
When you load the modules provided on Midway2 and Midway3 (e.g., `module load tensorflow`)
the CUDA dependency modules will be automatically loaded (comparing the output of `module list`
before and after doing `module load` command).

If you build the codes yourself using one of those CUDA modules,
remember to load these modules in your script.

Here is an example batch script that request GPU resources, loads
the CUDA libraries, and runs the MPI application. In this case, the application `your-app`
is in charge of supporting hybrid MPI/GPU parallelization.

```bash
#!/bin/bash

#SBATCH --job-name=test-gpu   # job name
#SBATCH --output=%N.out       # output log file
#SBATCH --error=%N.err        # error file
#SBATCH --time=01:00:00       # 1 hour of wall time
#SBATCH --nodes=1             # 1 GPU node
#SBATCH --ntasks-per-node=2   # 2 CPU cores to drive the GPUs
#SBATCH --partition=gpu2      # gpu2 partition
#SBATCH --gres=gpu:1          # Request 1 GPU per node


# Load all required modules below. As an example we load cuda/10.1
module load cuda/10.1

# Launch your run
mpirun -np 2 ./your-app input.txt
```

## Job Arrays

Slurm job arrays provide a convenient way to submit a large number of
independent processing jobs. For example, Slurm job arrays can be
useful for applying the same or similar computation to a collection of
data sets. Or, you can launch independent calculations each with
a different set of input parameters by submitting a single sbatch script.
When a job array script is submitted, a specified number of
array tasks are created based on the “master” sbatch script.

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

# Add lines here to run your computation on each job
./my_app -input $SLURM_ARRAY_TASK_ID
```

In this simple example, `--array=1-16` requests 16 array tasks
(numbered 1 through 16). The “array tasks” are copies of the master
script that are automatically submitted to the scheduler on your
behalf. In each array task, the environment variable
`SLURM_ARRAY_TASK_ID` is set to a unique value (in this
example, numbers ranging from 1 to 16). The application should be responsible to
use the array index to handle the corresponding data.

Job array indices can be specified in several different ways. Here are
some examples:

```default
# A job array with array tasks numbered from 0 to 31.
#SBATCH --array=0-31
```
or
```
# A job array with array tasks numbered 1, 2, 5, 19, 27.
#SBATCH --array=1,2,5,19,27
```
or
```
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
simultaneously. To achieve a higher throughput, consider [Parallel batch jobs](#parallel-batch).

For more information about Slurm job arrays, refer to [the Slurm documentation on job arrays](https://slurm.schedmd.com/job_array.html).

## Parallel Batch Jobs

Computations involving a very large number of independent computations
should be combined in some way to reduce the number of jobs submitted
to Slurm. Here we illustrate one strategy for doing this using [GNU
Parallel](http://www.gnu.org/software/parallel) and **srun**. The **parallel** program
executes tasks simultaneously until all tasks have been completed.

Here’s an example script, `parallel.sbatch`:

```bash
#!/bin/sh

#SBATCH --time=01:00:00
#SBATCH --partition=broadwl
#SBATCH --ntasks=28
#SBATCH --mem-per-cpu=2G  # NOTE DO NOT USE THE --mem= OPTION

# Load the default version of GNU parallel.
module load parallel

# When running a large number of tasks simultaneously, it may be
# necessary to increase the user process limit.
ulimit -u 10000

# This specifies the options used to run srun. The "-N1 -n1" options are
# used to allocates a single core to each task.
srun="srun --exclusive -N1 -n1"

# This specifies the options used to run GNU parallel:
#
#   --delay of 0.2 prevents overloading the controlling node.
#
#   -j is the number of tasks run simultaneously.
#
#   The combination of --joblog and --resume create a task log that
#   can be used to monitor progress.
#
parallel="parallel --delay 0.2 -j $SLURM_NTASKS --joblog runtask.log --resume"

# Run a script, runtask.sh, using GNU parallel and srun. Parallel
# will run the runtask script for the numbers 1 through 128. To
# illustrate, the first job will run like this:
#
#   srun --exclusive -N1 -n1 ./runtask.sh arg1:1 > runtask.1
#
$parallel "$srun ./runtask.sh arg1:{1} > runtask.sh.{1}" ::: {1..128}

# Note that if your program does not take any input, use the -n0 option to
# call the parallel command:
#
#   $parallel -n0 "$srun ./run_noinput_task.sh > output.{1}" ::: {1..128}

```

In this example, our aim is to run script `runtask.sh` 128
times. The `--ntasks` option is set to 28, so at most 28 tasks
can be run simultaneously.

Here is the `runtask.sh` script that is run by [GNU
Parallel](http://www.gnu.org/software/parallel):

```bash
#!/bin/sh

# This script outputs some useful information so we can see what parallel
# and srun are doing.

sleepsecs=$[ ( $RANDOM % 10 ) + 10 ]s

# $1 is arg1:{1} from GNU parallel.
#
# $PARALLEL_SEQ is a special variable from GNU parallel. It gives the
# number of the job in the sequence.
#
# Here we print the sleep time, host name, and the date and time.
echo task $1 seq:$PARALLEL_SEQ sleep:$sleepsecs host:$(hostname) date:$(date)

# Sleep a random amount of time.
sleep $sleepsecs
```

To submit this job, copy both `parallel.sbatch` and
`runtask.sh` to the same directory, and run `chmod +x
runtask.sh` to make `runtask.sh` executable. Then the job can be
submitted to the Slurm queue:

```default
sbatch parallel.sbatch
```

When this job completes, you should see output files with names
`runtask.sh.N`, where `N` is a number between 1 and 128. The
content of the first output file (i.e., `runtask.sh.1`) should look
something like this:

```default
task arg1:1 seq:1 sleep:14s host:midway2-0002 date:Thu Jan 10 09:17:36 CST 2017
```

Another file `runtask.log` is also created. It gives a list of
the completed jobs. (Note: If the sbatch is submitted again, nothing
will be run until `runtask.log` is removed.)

It is also possible to use this same technique to run multithreaded
tasks in parallel. Here is an example sbatch script,
`parallel-hybrid.sbatch`, that distributes multithreaded
computations (each using 28 CPUs) across 2 nodes:

```bash
#!/bin/sh

#SBATCH --partition=broadwl
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --exclusive

# Load the default version of GNU parallel.
module load parallel

srun="srun --exclusive -N1 -n1 --cpus-per-task $SLURM_CPUS_PER_TASK"

# Instead of $SLURM_NTASKS, use $SLURM_NNODES to determine how
# many jobs should be run simultaneously.
parallel="parallel --delay 0.2 -j $SLURM_NNODES --joblog runtask.log --resume"

# Run the parallel command.
$parallel "$srun ./runtask.sh arg1:{1} > runtask.sh.{1}" ::: {1..6}

```

## Cron-like Jobs

Cron-like jobs are jobs that are submitted to the queue with a specified schedule.
These jobs persist until they are canceled or encounter an error.
The Midway2 cluster has a dedicated partition, `cron`, for running
Cron-like jobs. Please email [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu)
to request submitting Cron-like jobs. These jobs are subject to scheduling limits and will
be monitored.

Here is an example of a batch script that internally submits a Cron job (`cron.sbatch`):

```bash
#!/bin/bash

#SBATCH --time=00:05:00
#SBATCH --output=cron.log
#SBATCH --open-mode=append
#SBATCH --account=cron-account
#SBATCH --partition=cron
#SBATCH --qos=cron

# Specify a valid Cron string for the schedule. This specifies that
# the Cron job run once per day at 5:15a.
SCHEDULE='15 5 * * *'

# Here is an example of a simple command that prints the host name and
# the date and time.
echo "Hello on $(hostname) at $(date)."

# This schedules the next run.
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron.sbatch
```

After executing a simple command (print the host name, date and time),
the script schedules the next run with another call to `sbatch` with
the `--begin` option.

## Dependency Jobs

You can schedule jobs that are dependend upon the termination status of
other previously scheduled jobs. This way you can concatenate your jobs into a pipeline,
or even expand to more complicated dependencies.

For example, `job1.sbatch` is a submission script you plan to
submit a batch job to Midway:

```bash
#!/bin/bash

#SBATCH --job-name=hellompi
#SBATCH --output=hellompi.out
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --partition=broadwl

# Load the MPI module that was used to build the application
module load openmpi

mpirun -np 32 ./hellompi

```

Submit the job script to the Slurm job scheduler from a Midway login node:

```
sbatch job1.sbatch
```

which returns the job ID, for example, `1234567`.

You can then submit another job that is put on the waiting list of the queue (pending)

```
sbatch -dependency=afterany:1234567 job2.sbatch
```

This command indicates that `job2.sbatch` will be put in the queue after the job ID `1234567`
is terminated for any reason. The dependency option flag can be `after`, `afterany`, `afterok`
and `afternotok`, which are self-explanatory.

For more information of job dependencies, please refer to
the [Slurm documenation](https://slurm.schedmd.com/sbatch.html).