Running jobs on DaLi
====================

This section of DaLi user guide is about running computations on the DaLi compute nodes. All jobs running on compute nodes consume Service Units (SUs); see [RCC Service Units](https://rcc.uchicago.edu/getting-started/user-guidelines) for more information.

Login nodes vs. compute nodes
-----------------------------

Once you have connected to DaLi, you may work on one of the login nodes. Login nodes may be used for compiling and debugging code, installing software, editing and managing files, submitting jobs, or any other work that is not long-running or computationally intensive. *Login nodes should not be used for computionally intensive work*.

The Midway compute cluster, including DaLi, uses a scheduler to manage requests for access to compute resources. These requests are called jobs. In particular, we use the [Slurm](http://slurm.schedmd.com/) resource manager to schedule jobs as well as interactive access to compute nodes.

Here, we give the essential information you need to know to start computing on Midway. For more detailed information on running specialized compute jobs, see [Running jobs on Midway](https://rcc.uchicago.edu/docs/running-jobs/index.html#running-jobs).

Service Units and Allocations
-----------------------------

Service Units (SUs) are a measure of the amount of computing resources consumed on a compute cluster. Computing resources in a compute cluster include processing units (also called CPUs or cores), memory, and Graphical Processing Units (GPUs). The aim of the Service Unit (SU) is to provide a “fair” account of computing resources. For more information, please refer to the [RCC Service Units](https://rcc.uchicago.edu/getting-started/user-guidelines) webpage.

An “allocation” is a quantity of computing time (SUs) and storage resources that are granted to a group of users, usually a lab managed by a principal investigator (PI). Without an allocation, you cannot schedule and run jobs on the RCC compute cluster. For more information about SU allocations, see [RCC Allocations](https://rcc.uchicago.edu/getting-started/request-allocation).

Checking your account balance
-----------------------------

The rcchelp tool can be used to check account balances. After logging into Midway, simply type:

```
$ rcchelp balance
```

If you are a member of multiple groups, this will display the allocations and usage for all your groups. The `rcchelp balance` command has a number of options for summarizing allocation usage. For information on these options, type

```
$ rcchelp balance --help
```

To see an overall summary of your usage, simply enter:

```
$ rcchelp usage
```

You can also get a more detailed breakdown of your usage by job using the `--byjob` option:

```
$ rcchelp usage --byjob
```

For more options available in the `rcchelp` tool, type

```
$ rcchelp --help
```

Types of Compute Nodes
----------------------

The Midway compute cluster, including DaLi, is made up of compute nodes with a variety architectures and configurations. Currently, DaLi has 30 nodes with the following specifications:

| Cluster | Partition | Compute cores (CPUs) per node  | Memory     | Other configuraiton details         |
|:--------|:----------|:-------------------------------|:-----------|:------------------------------------|
| Dali    | `dali`    | 2 SkyLake processors (40 CPUs) | 64 GB DDR4 | EDR and FDR Infiniband interconnect |

Interactive Jobs
----------------

After submitting an “interactive job” on Midway, the Slurm job scheduler will connect you to a compute node, and will load up an interactive shell environment for you to use on that compute node. This interactive session will persist until you disconnect from the compute node, or until you reach the maximum requested time. The default requested time is 2 hours.

### `sinteractive`

The command `sinteractive` is the recommended Slurm command for requesting an interactive session. As soon as the requested resources become available, `sinteractive` will do the following:

-	Log in to the node.
-	Change into the directory you were working in.
-	Set up X11 forwarding for displaying graphics.
-	Transfer your current shell environment, including any modules you have previously loaded.

To get started (with the default interactive settings), simply enter `sinteractive` in the command line:

```
$ sinteractive
```

By default, an interactive session times out after 2 hours. If you would like more than 2 hours, be sure to include a --`time=HH:MM:SS` flag to specify the necessary amount of time. For example, to request an interactive session for 6 hours, run the following command:

```
$ sinteractive --time=06:00:00
```

There are many additional options for the `sinteractive` command, including options to select the number of nodes, the number of cores per node, the amount of memory, and so

```
$ sinteractive --exclusive --partition=dali --nodes=2 --time=08:00:00
```

For more details about these and other useful options, read below about the `sbatch` command, and see Running jobs on midway. Note that all options available in the `sbatch` command are also available for the `sinteractive` command.

### srun

An alternative to the `sinteractive` command is the `srun` command:

```
$ srun --pty bash
```

Unlike `sinteractive`, this command does not set up X11 forwarding, which means you cannot display graphics using `srun`. Both the `srun` and `sinteractive` commands have the same command options.

### Batch Jobs¶

The `sbatch` command is the command most commonly used by RCC users to request computing resources on the Midway cluster including DaLi. Rather than specify all the options in the command line, users typically write an sbatch script that contains all the commands and parameters necessary to run the program on the cluster.

In an sbatch script, all Slurm parameters are declared with `#SBATCH`, followed by additional definitions.

Here is an example of an sbatch script:

```
#!/bin/bash
#SBATCH --job-name=example_sbatch
#SBATCH --output=example_sbatch.out
#SBATCH --error=example_sbatch.err
#SBATCH --time=00:05:00
#SBATCH --partition=dali
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=20
#SBATCH --mem-per-cpu=3000
#SBATCH --account=pi-rcc

module load openmpi
mpirun ./hello-mpi
```

Here is an explanation of what each of these options does:

| Option                                | Description                                                                                                 |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------|
| `#SBATCH --job-name=example_sbatch`   | Assigns label example_sbatch to the job.                                                                    |
| `#SBATCH --output=example_sbatch.out` | Writes console output to file example_sbatch.out.                                                           |
| `#SBATCH --error=example_sbatch.err`  | Writes an error messages to file example_sbatch.err.                                                        |
| `#SBATCH --time=01:30:00`             | Reserves the computing resources for 1 hour and 30 minutes (or less if program completes before 1.5 hours). |
| `#SBATCH --partition=dali`            | Requests compute nodes from the DaLi partition on the Midway cluster.                                       |
| `#SBATCH --nodes=4`                   | Requests 4 compute nodes.                                                                                   |
| `#SBATCH --ntasks-per-node=20`        | Requests 20 cores (CPUs) per node, for a total of 20 * 4 = 80 cores.                                        |
| `#SBATCH --mem-per-cpu=3000`          | Requests 3000 MB (3 GB) of memory (RAM) per core, for a total of 3 * 20 = 60 GB per node.                   |
| `#SBATCH --account=pi-rcc`            | Use SU from the pi-rcc account allocation.                                                                  |

In this example, we have requested 4 compute nodes with 20 CPUs each. Therefore, we have requested a total of 60 CPUs for running our program. The last two lines of the script load the OpenMPI module and launch the MPI-based executable that we have called `hello-mpi` (see [MPI jobs](https://rcc.uchicago.edu/docs/running-jobs/mpi/index.html#mpi-jobs)).

Continuing the example above, suppose that this script is saved in the current directory into a file called `example.sbatch`. This script is submitted to the cluster using the following command:

```
$ sbatch ./example.sbatch

```

Many other options are available for submitting jobs using the `sbatch` command. For more specialized computational needs, see [Running jobs on midway](https://rcc.uchicago.edu/docs/running-jobs/index.html#running-jobs). Additionally, for a complete list of the available options, see the [Official SBATCH Documentation](http://slurm.schedmd.com/sbatch.html).

### Managing Jobs

The Slurm job scheduler provides several command-line tools for checking on the status of your jobs and for managing them. For a complete list of Slurm commands, see the [Slurm man pages](http://slurm.schedmd.com/man_index.html). Here are a few commands that you may find particularly useful:

-	`squeue`: finds out the status of jobs submitted by you and other users.
-	`sacct`: retrieves job history and statistics about past jobs.
-	`scancel`: cancels jobs you have submitted.

In the next couple sections we explain how to use `squeue` to find out the status of your submitted jobs, and `scancel` to cancel jobs in the queue.

#### Checking your jobs

Use the `squeue` command to check on the status of your jobs, and other jobs running on Midway. The simplest invocation lists all jobs that are currently running or waiting in the job queue (“pending”), along with details about each job such as the job id and the number of nodes requested:

```
$ squeue
```

Any job with `0:00` under the `TIME` column is a job that is still waiting in the queue.

To view only the jobs that you have submitted, use the `--user` flag

```
$ squeue --user=$USER
```

This command has many other useful options for querying the status of the queue and getting information about individual jobs. For example, to get information about all jobs that are waiting to run on DaLi partition, enter:

```
$ squeue --state=PENDING --partition=dali
```

Alternatively, to get information about all your jobs that are running on the DaLi partition, type:

```
$ squeue --state=RUNNING --partition=dali --user=$USER
```

The last column of the output tells us which nodes are allocated for each job. For example, if it shows `dali-012` for one of the jobs under your name, you may type `ssh DaLI-012` to log in to that compute node and inspect the progress of your computation locally.

For more information, consult the command-line help by typing `squeue --help`, or visit the official online documentation.

#### Canceling your jobs

To cancel a job you have submitted, use the `scancel` command. This requires you to specify the id of the job you wish to cancel. For example, to cancel a job with `id 8885128`, do the following:

```
$ scancel 8885128
```

If you are unsure what is the id of the job you would like to cancel, see the JOBID column from running `squeue --user=$USER`.

To cancel all jobs you have submitted that are either running or waiting in the queue, enter the following:

```
$ scancel --user=$USER
```

#### Job Limits

To distribute computational resources fairly to all Midway users even among DaLi users, the RCC sets limits on the amount of computing resources that may be requested by a single user at any given time.

On DaLi, the maximum run-time for an individual job is 36 hours. The maximum number of jobs per user is 200 and the maximum number of jobs that each user can submit is 500. These apply to all batch and interactive jobs submitted to DaLi compute nodes.

### Temporary File Storage

Many applications generate temporary or intermediate files that are written to `/tmp`. (These applications may write files to `/tmp` even without you being aware that this is happening.) This folder is typically on a local drive or the RAM disk that virtualized in the system memory.

Contents in `/tmp` left by a user’s job won’t be automatically purged before rebooting the corresponding node, and therefore may affect other jobs later running on the same node. Therefore, RCC enforces a data purge policy for files written to `/tmp` on compute nodes:

1.	For each running job, a special “job-protected” folder `/tmp/jobs/${SLURM_JOB_ID}` is created on each allocated node. Its contents are safely purged only upon termination of the job (when it is sucessfully completed, canceled or killed).

2.	For any running jobs, environment variables `SLURM_TMPDIR` and `TMPDIR` are set to `/tmp/jobs/${SLURM_JOB_ID}`. Whenever possible, users should write to the paths specified by these environment variables rather than using `/tmp` explicitly. (Most applications should already be using these environment variables by default, so in many cases this will not require any change to your code.)

3.	In addition to using `$TMPDIR`, users should also verify that no additional files are being written to `/tmp`.

4.	Note that upon termination of a job, any folders or files directly under `/tmp` that belong to the submitter of this job will be purged.

5.	The contents of `/tmp` do not persist after jobs terminate. The RCC is not responsible for retrieving or recovering data stored there. For critical outputs, please save them to the persisent file storage systems.

Note: Folders or files created by users in `/tmp` outside `$TMPDIR` are NOT job-protected. For example, consider the case when user has two running jobs (A and B) on the same node, and job B is directly writing files in `/tmp`. If job A terminates before job B, the contents of `/tmp` will be also purged, and in some cases may cause job B to fail. To avoid failure, users should therefore write any temporary data to the job-protected folder, `SLURM_TMPDIR` or `TMPDIR`.
