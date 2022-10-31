# Illustrative examples

Below are a number of example submission scripts that you can adapt to
run your jobs on Midway. See also the materials from the
[RCC Slurm workshop](https://github.com/rcc-uchicago/SLURM_WORKSHOP)
for additional examples.

## Job arrays

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
## Large-memory jobs

The `bigmem2` partition is particularly well suited for computations
that need more than about 60 GB of memory; see [Types of Compute Nodes](../../using-midway/index.md#node-types) for
technical specifications of the bigmem2 nodes.

### Running a large-memory job

To submit a job to bigmem2, include this line in your sbatch script:

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

### Interactive computing on bigmem2

These same options can also be used to set up an sinteractive
session. For example, to access a bigmem2 node with 1 CPU
and 128 GB of memory, run:

```bash
sinteractive --partition=bigmem2 --ntasks=1 --cpus-per-task=8 --mem=128G
```

## Parallel batch jobs

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

Here is the `runtask.sh` script that is run by GNU parallel:

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

## MPI jobs

Here we present a couple small examples illustrating how to use MPI
for distributed computing Midway. For more information on the MPI
libraries available on Midway, see [Message Passing Interface (MPI)](../../software/libraries/mpi/index.md#mpi-libraries).

Our main illustration is a “hello world” example. See file
`hellompi.c` for the C code we will compile and run.

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

Copy `hellompi.c` to your home directory on Midway, load the
default OpenMPI module, and compile the program on a Midway login
node:

```default
module load openmpi
mpicc hellompi.c -o hellompi
```

`hellompi.sbatch` is a submission script that can be used to
submit a job to Midway to run the `hellompi` program:

```bash
#!/bin/bash

#SBATCH --job-name=hellompi
#SBATCH --output=hellompi.out
#SBATCH --ntasks=56
#SBATCH --partition=broadwl
#SBATCH --constraint=fdr

# Load the default OpenMPI module.
module load openmpi

# Run the hellompi program with mpirun. The -n flag is not required;
# mpirun will automatically figure out the best configuration from the
# Slurm environment variables.
 mpirun ./hellompi

```

Submit the MPI job to the Slurm job scheduler from a Midway login
node:

```default
sbatch hellompi.sbatch
```

Here is an example output:

```default
Process 1 on midway2-0172.rcc.local out of 56
Process 3 on midway2-0172.rcc.local out of 56
Process 5 on midway2-0172.rcc.local out of 56
Process 7 on midway2-0172.rcc.local out of 56
Process 6 on midway2-0172.rcc.local out of 56
Process 9 on midway2-0172.rcc.local out of 56
Process 10 on midway2-0172.rcc.local out of 56
Process 11 on midway2-0172.rcc.local out of 56
Process 13 on midway2-0172.rcc.local out of 56
Process 0 on midway2-0172.rcc.local out of 56
Process 2 on midway2-0172.rcc.local out of 56
Process 4 on midway2-0172.rcc.local out of 56
Process 8 on midway2-0172.rcc.local out of 56
Process 12 on midway2-0172.rcc.local out of 56
Process 17 on midway2-0173.rcc.local out of 56
Process 19 on midway2-0173.rcc.local out of 56
Process 21 on midway2-0173.rcc.local out of 56
Process 28 on midway2-0173.rcc.local out of 56
Process 29 on midway2-0173.rcc.local out of 56
Process 31 on midway2-0173.rcc.local out of 56
Process 32 on midway2-0173.rcc.local out of 56
Process 15 on midway2-0173.rcc.local out of 56
Process 18 on midway2-0173.rcc.local out of 56
Process 20 on midway2-0173.rcc.local out of 56
Process 22 on midway2-0173.rcc.local out of 56
Process 23 on midway2-0173.rcc.local out of 56
Process 24 on midway2-0173.rcc.local out of 56
Process 52 on midway2-0175.rcc.local out of 56
Process 25 on midway2-0173.rcc.local out of 56
Process 53 on midway2-0175.rcc.local out of 56
Process 26 on midway2-0173.rcc.local out of 56
Process 54 on midway2-0175.rcc.local out of 56
Process 27 on midway2-0173.rcc.local out of 56
Process 55 on midway2-0175.rcc.local out of 56
Process 14 on midway2-0173.rcc.local out of 56
Process 16 on midway2-0173.rcc.local out of 56
Process 30 on midway2-0173.rcc.local out of 56
Process 43 on midway2-0174.rcc.local out of 56
Process 51 on midway2-0174.rcc.local out of 56
Process 48 on midway2-0174.rcc.local out of 56
Process 49 on midway2-0174.rcc.local out of 56
Process 46 on midway2-0174.rcc.local out of 56
Process 44 on midway2-0174.rcc.local out of 56
Process 45 on midway2-0174.rcc.local out of 56
Process 40 on midway2-0174.rcc.local out of 56
Process 42 on midway2-0174.rcc.local out of 56
Process 36 on midway2-0174.rcc.local out of 56
Process 37 on midway2-0174.rcc.local out of 56
Process 47 on midway2-0174.rcc.local out of 56
Process 34 on midway2-0174.rcc.local out of 56
Process 38 on midway2-0174.rcc.local out of 56
Process 35 on midway2-0174.rcc.local out of 56
Process 39 on midway2-0174.rcc.local out of 56
Process 41 on midway2-0174.rcc.local out of 56
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
Process 0 on midway2-0002.rcc.local out of 56
Process 13 on midway2-0052.rcc.local out of 56
Process 2 on midway2-0013.rcc.local out of 56
Process 9 on midway2-0033.rcc.local out of 56
Process 54 on midway2-0177.rcc.local out of 56
Process 53 on midway2-0176.rcc.local out of 56
Process 44 on midway2-0157.rcc.local out of 56
Process 55 on midway2-0178.rcc.local out of 56
Process 11 on midway2-0041.rcc.local out of 56
Process 40 on midway2-0152.rcc.local out of 56
Process 43 on midway2-0156.rcc.local out of 56
Process 45 on midway2-0161.rcc.local out of 56
Process 46 on midway2-0162.rcc.local out of 56
Process 38 on midway2-0147.rcc.local out of 56
Process 39 on midway2-0148.rcc.local out of 56
Process 24 on midway2-0101.rcc.local out of 56
Process 3 on midway2-0014.rcc.local out of 56
Process 42 on midway2-0155.rcc.local out of 56
Process 51 on midway2-0174.rcc.local out of 56
Process 36 on midway2-0145.rcc.local out of 56  
Process 25 on midway2-0102.rcc.local out of 56
Process 16 on midway2-0055.rcc.local out of 56
Process 18 on midway2-0057.rcc.local out of 56
Process 12 on midway2-0051.rcc.local out of 56
Process 14 on midway2-0053.rcc.local out of 56
Process 4 on midway2-0015.rcc.local out of 56
Process 15 on midway2-0054.rcc.local out of 56
Process 48 on midway2-0164.rcc.local out of 56
Process 28 on midway2-0105.rcc.local out of 56
Process 22 on midway2-0097.rcc.local out of 56
Process 30 on midway2-0118.rcc.local out of 56
Process 1 on midway2-0012.rcc.local out of 56
Process 35 on midway2-0144.rcc.local out of 56
Process 17 on midway2-0056.rcc.local out of 56
Process 37 on midway2-0146.rcc.local out of 56
Process 32 on midway2-0141.rcc.local out of 56
Process 34 on midway2-0143.rcc.local out of 56
Process 27 on midway2-0104.rcc.local out of 56
Process 31 on midway2-0119.rcc.local out of 56  
Process 29 on midway2-0106.rcc.local out of 56
Process 10 on midway2-0034.rcc.local out of 56
Process 47 on midway2-0163.rcc.local out of 56
Process 33 on midway2-0142.rcc.local out of 56
Process 26 on midway2-0103.rcc.local out of 56
Process 7 on midway2-0019.rcc.local out of 56
Process 20 on midway2-0073.rcc.local out of 56
Process 5 on midway2-0016.rcc.local out of 56
Process 8 on midway2-0027.rcc.local out of 56
Process 41 on midway2-0153.rcc.local out of 56
Process 6 on midway2-0017.rcc.local out of 56
Process 21 on midway2-0096.rcc.local out of 56
Process 19 on midway2-0072.rcc.local out of 56
Process 23 on midway2-0100.rcc.local out of 56
```

### Additional notes

Both OpenMPI and IntelMPI have the ability to launch MPI programs
directly with the Slurm command **srun**. It is not necessary to use this mode for most jobs, but it may provide additional job
launch options. For example, from a Midway login node it is possible
to launch the above `hellompi` program using OpenMPI using 28
MPI processes:

```default
srun -n28 hellompi
```

With IntelMPI, you need to also set an environment variable for this
to work:

```default
export I_MPI_PMI_LIBRARY=/software/slurm-current-$DISTARCH/lib/libpmi.so
srun -n28 hellompi
```

## Hybrid MPI/OpenMP jobs

MPI and OpenMP can be used at the same time to create a Hybrid
MPI/OpenMP program.

Let’s look at an example Hybrid MPI/OpenMP hello world program and
explain the steps needed to compile and submit it to the queue. An
example hybrid MPI hello world program: `hellohybrid.c`

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

To run the program on the RCC cluster, copy `hellohybrid.c` and
`hellohybrid.sbatch` to your home directory, then compile the code
interactively by entering the following commands into a terminal on a
Midway2 login node:

```default
module load openmpi
mpicc -fopenmp hellohybrid.c -o hellohybrid
```

Here we load the default MPI compiler, but it should be possible to
use any available MPI compiler to compile and run this example. Note
that the option `-fopenmp` must be used here to compile the
program because the code includes OpenMP directives (use
`-openmp` for the Intel compiler and `-mp` for the PGI
compiler).

`hellohybrid.sbatch` is a submission script that can be used
to submit a job to Midway2 to run the `hellohybrid` program.

```bash
#!/bin/bash

# A job submission script for running a hybrid MPI/OpenMP job on
# Midway2.
             
#SBATCH --job-name=hellohybrid
#SBATCH --output=hellohybrid.out
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=8
#SBATCH --partition=broadwl
#SBATCH --constraint=edr

# Load the default OpenMPI module.
module load openmpi

# Set OMP_NUM_THREADS to the number of CPUs per task we asked for.
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run the process with mpirun. Note that the -n option is not required
# in this case; mpirun will automatically determine how many processes
# to run from the Slurm settings.
mpirun ./hellohybrid

The options are similar to running an MPI job, with some differences:


* `--ntasks=4` specifies the number of MPI processes (“tasks”).


* `--cpus-per-task=8` allocates 8 CPUs for each task.


* `export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK` sets the number of
OpenMP threads to the number of requested cores (CPUs) for each
task.

You can submit `hellohybrid.sbatch` using the following
command from one of Midway2 login nodes:


```default
sbatch hellohybrid.sbatch
```

Here is an example output of this program submitted to the `broadwl`
partition on Midway2:

```bash
Hello from thread 0 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 6 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 0 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 7 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 3 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 2 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 3 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 4 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 5 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 1 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 7 out of 8 from process 0 out of 4 on midway2-0269.rcc.local
Hello from thread 2 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 1 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 4 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 5 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 6 out of 8 from process 1 out of 4 on midway2-0269.rcc.local
Hello from thread 0 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 7 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 4 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 5 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 1 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 6 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 3 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 2 out of 8 from process 2 out of 4 on midway2-0269.rcc.local
Hello from thread 0 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 7 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 4 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 6 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 2 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 5 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
Hello from thread 1 out of 8 from process 3 out of 4 on midway2-0270.rcc.local
```
## GPU jobs

The `gpu2` partition is dedicated to software that uses Graphical
Processing Units (GPUs). See [Types of Compute Nodes](../../using-midway/index.md#node-types) for technical
specifications of the gpu2 nodes.

CUDA and OpenACC are two widely used tools for developing GPU-based
software. For information on compiling code with CUDA and OpenACC, see
[CUDA and OpenACC Compilers](../../software/compilers/nvidia/index.md#gpu-compiling).

### Running GPU code on Midway2

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
## Cron-like jobs

Cron jobs persist until they are canceled or encounter an error.
The Midway2 cluster has a dedicated partition, `cron`, for running
Cron jobs. Please email [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu) to request submitting
Cron-like jobs. These jobs are subject to scheduling limits and will
be monitored.

Here is an example of an sbatch script that runs a Cron job (see also
`cron.sbatch`):

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
