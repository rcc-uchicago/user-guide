# Parallel batch jobs

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
        
                                 