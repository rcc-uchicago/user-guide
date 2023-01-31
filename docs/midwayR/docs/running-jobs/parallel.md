# Parallel Batch Jobs

Batch jobs that consist of large number of serial jobs should most likely be combined in some way to optimize the job submission and reduce the number of submitted jobs to a more manageable number.

RCC has developed a method to handle this type of job submissions using [GNU Parallel](http://www.gnu.org/software/parallel/) and **srun**. For this submission method, a single job is submitted with a chosen number of CPU cores allocated (using the Slurm option `--ntasks=X`) and the parallel command is used to run that number of tasks simultaneously until all tasks have been completed.

An example submit file is `parallel.sbatch`:

```bash
#!/bin/sh

#SBATCH --time=01:00:00
#SBATCH --ntasks=32

module load parallel

# for a large number of tasks, the controlling node will have a large number
# of processes, so it will be necessary to change the user process limit
ulimit -u 10000

# the --exclusive to srun make srun use distinct CPUs for each job step
# -N1 -n1 allocates a single core to each task
srun="srun --exclusive -N1 -n1"

# --delay .2 prevents overloading the controlling node
# -j is the number of tasks parallel runs so we set it to $SLURM_NTASKS
# --joblog makes parallel create a log of tasks that it has already run
# --resume makes parallel use the joblog to resume from where it has left off
# the combination of --joblog and --resume allow jobs to be resubmitted if
# necessary and continue from where they left off
# NOTE: if you want to run your job again, you will need to delete the runtask.log file
parallel="parallel --delay .2 -j $SLURM_NTASKS --joblog runtask.log --resume"

# this runs the parallel command we want
# in this case, we are running a script named runtask
# parallel uses ::: to separate options. Here {1..128} is a shell expansion
# so parallel will run the runtask script for the numbers 1 through 128
# {1} is the first argument
# as an example, the first job will run like this:
# srun --exclusive -N1 -n1 ./runtask arg1:1 > runtask.1
$parallel "$srun ./runtask arg1:{1} > runtask.{1}" ::: {1..128}

# if your program does not take any input, use -n0 option to call the parallel
# command as follows:
# $parallel -n0 "$srun ./runnoinptask > output.{1}" ::: {1..128}
```

In this submit file we want to run the runtask script 128 times. The `--ntasks` option is set to 32, so we are allocating 1/4th the number of CPU cores as tasks that we want to run. **parallel** will run the first 32 tasks on 32 cores and then as CPU cores become available it will run the rest of tasks.

Parallel is very flexible in what can be used as the command line arguments. In this case we are using a simple shell expansion of the numbers 1 through 128, but arguments can be piped into the **parallel** command, arguments could be file names instead of numbers, replacements can be made, and much more. Reading the [Parallel Manual](http://www.gnu.org/software/parallel/man.html) will provide full details on its capabilities.

Here is the `runtask` script that **parallel** runs.

```bash
#!/bin/sh

# this script echoes some useful outputs so we can see what parallel
# and srun are doing

sleepsecs=$[ ( $RANDOM % 10 )  + 10 ]s

# $1 is arg1:{1} from parallel.
# $PARALLEL_SEQ is a special variable from parallel. It is the actual sequence
# number of the job regardless of the arguments given
# We print the sleep time, hostname, and date for more info
echo task $1 seq:$PARALLEL_SEQ sleep:$sleepsecs host:$(hostname) date:$(date)

# sleep a random amount of time
sleep $sleepsecs
```

To submit this job, download both the `parallel.sbatch` and `runtask` scripts and put them in the same directory. Run the `chmod +x runtask` command to make sure `runtask` is executatble. Then, the job can be submitted like this:

```bash
sbatch parallel.sbatch
```

When this job completes, there should be 128 `runtask.N` output files where `N` is a number between 1 and 128. The content of the first output file (i.e., `runtask.1`) will look similar to this (numbers and the host name will likely be different):

```
task arg1:1 seq:1 sleep:14s host:midway2-0002 date:Thu Jan 10 09:17:36 CST 2017
```

A file named `runtask.log` will also be created that lists the completed jobs. NOTE: If this job is resubmitted, nothing will be run until the `runtask.log` file is removed.

It is also possible to use this technique to run tasks that are either multi-threaded or can otherwise use more than one CPU at a time. Here is an example submit file:

```bash
#!/bin/sh

#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --exclusive

module load parallel

# For this mode add -c (--cpus-per-task) to the srun command
srun="srun --exclusive -N1 -n1 -c$SLURM_CPUS_PER_TASK"

# Instead of $SLURM_NTASKS we want to use $SLURM_NNODES to tell
# parallel how many jobs to start
parallel="parallel --delay .2 -j $SLURM_NNODES --joblog runtask.log --resume"

# run the parallel command again. The runtask command should be able to use the
# 28 cpus we requested with -c28 by itself
$parallel "$srun ./runtask arg1:{1} > runtask.{1}" ::: {1..6}
```

In this case, the `runtask` script itself will use 28 CPUs and **parallel** distributes 6 of these jobs to the 2 requested nodes.