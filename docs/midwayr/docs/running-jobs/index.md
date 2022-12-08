# Running jobs on midwayR

This section of the documentation describes how to run your jobs on the compute nodes
of MidwayR. 

# Login nodes vs. compute nodes

Upon connecting to midwayR, you will be located on one of the two midwayR login nodes. Login nodes may be used for compiling and debugging code, installing software, editing and managing files, submitting jobs, or any other work that is not long-running or computationally intensive. Login nodes should not be used for computionally intensive work.

All intensive computations should be performed on compute nodes. Access to compute nodes can be obtained by submitting a job through the Slurm scheduler, or by requesting an interactive session. If you are unsure whether your computations will be intensive, please request an interactive session and continue your work once you have connected to the compute node.

> **Note** Running computationally intensive jobs on the midwayR login nodes prevents other users from efficiently using the cluster. RCC System Administrators may terminate your processes without warning if your processes disrupt other users’ work on the RCC cluster.

# Requesting Compute Resources for your Job
The MidwayR compute resources rely on a job scheduler to manage requests for access
to the compute resources. These requests are called jobs. In particular, we use the
[Slurm](https://slurm.schedmd.com/) resource manager to schedule both interactive
access and batch job submission to the compute nodes.

Here, we give the minimal information you will need to know to start computing
on MidwayR. The compute resources are managed by the Slurm job scheduler. There 
are two ways of making use of the compute resources. Your jobs can make use of 
the compute ressources of MidwayR either through an interactive session or by 
a non-interactive batch job submission. Both of these two ways of utilizing the
compute resources are described below. 

## Interactive jobs
An interactive job is a job that allows users to interact with requested resources
in real time. Users can run their analysis, execute their software, or run other 
commands directly on a compute node. 

The command ``sinteractive`` is the recommended Slurm command for
requesting an interactive session. As soon as the requested resources
become available, sinteractive will do the following:

1. Log in to the compute node.
2. Change into the directory you were working in.
3. Set up X11 forwarding for displaying graphics if this is enabled.
4. Transfer your current shell environment, including any modules you
   have previously loaded.

To get started (with the default interactive settings), simply enter
`sinteractive` in the command line: 

```bash
  $ sinteractive
```

If you are a MidwayR researcher affiliated with the Booth School of Business, you are entitled to Booth purchased 
harware resources. To use Booth dedicated MidwayR resources, please specify partition 'booth', as the following,


```bash
  $ sinteractive --partition=booth
```

By default, an interactive session times out after 2 hours.  If you
would like more than 2 hours, be sure to include a ``--time=HH:MM:SS``
flag to specify the necessary amount of time. For example, to request
an interactive session for 6 hours, run the following command: 

```bash
  $ sinteractive --time=06:00:00
```

There are many additional options for the ``sinteractive`` command,
including options to select the number of nodes, the number of cores
per node, the amount of memory, and so on.  For example, to request
exclusive use of two compute nodes equipped with the Infiniband
interconnect on the Midway1 **sandyb** partition for 8 hours, enter
the following: 

```bash
  $ sinteractive --exclusive  --nodes=2  --time=08:00:00
```

For more details about these and other useful options, see below
about the ``sbatch`` command, and see the illustrative sbatch examples below.
Note that all options available in the ``sbatch`` command are also available for
the ``sinteractive`` command.

### srun

An alternative to the ``sinteractive`` command is the ``srun`` command: 

```bash
  $ srun --pty bash
```

Unlike ``sinteractive``, this command does not set up X11 forwarding,
which means you cannot display graphics using ``srun``. Both the
``srun`` and ``sinteractive`` commands have the same command options.


## Batch Jobs

The ``sbatch`` command is the command most commonly used by RCC users
to request computing resources on the Midway cluster. Rather than
specify all the options in the command line, users typically write an
"sbatch script" that contains all the commands and parameters
neccessary to run the program on the cluster.

In an sbatch script, all Slurm parameters are declared with ``#SBATCH``,
followed by additional definitions.

Here is an example of an sbatch script:

```bash
  #!/bin/bash
  #SBATCH --job-name=example_sbatch
  #SBATCH --output=example_sbatch.out
  #SBATCH --error=example_sbatch.err
  #SBATCH --time=00:05:00
  #SBATCH --partition=skylake
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=40
  #SBATCH --mem-per-cpu=2000

  module load Anaconda3
  python myjob.py
```


Here is an explanation of what each of these options does:

| Option  | Description  |
|---|---|
| `#SBATCH --job-name=example_sbatch`   | Assigns label `example_sbatch` to the job.  |
| `#SBATCH --output=example_sbatch.out` | Writes console output to file `example_sbatch.out`. |
| `#SBATCH --error=example_sbatch.err`  | Writes an error messages to file `example_sbatch.err`.    |
| `#SBATCH --time=00:05:00`             | Reserves the computing resources for 5 minutes (or less if program completes before 5 min). |
| `#SBATCH --partition=skylake`         | Requests compute nodes from the `skylake` partition on the MidwayR cluster.  (Noted, If you are a MidwayR researcher affiliated with the Booth School of Business, you have access to `Booth` partition in addition to `skylake`. Booth researchers can use `#SBATCH --partition=booth` in this line for better computational performance.) |
| `#SBATCH --nodes=2`                   | Requests 2 compute nodes.       |
| `#SBATCH --ntasks-per-node=40`        | Requests 40 cores (CPUs) per node, for a total of 40 * 2 = 80 cores.  |
| `#SBATCH --mem-per-cpu=2000`          | Requests 2000 MB (2 GB) of memory (RAM) per core, for a total of 2 * 40 = 80 GB per node. |

 To use Booth dedicated MidwayR resources, please specify partition 'booth', as the following,



In this example, we have requested 2 compute nodes with 40 CPU cores
each. Therefore, we have requested a total of 80 CPU cores for running our
program. The last two lines of the script load the Anaconda3 module and
launch the python executable that we have called ``myjob.py``

> **Note** If the `--partition` option is not specified, the request will 
automatically be directed to the ``skylake`` partition on MidwayR. 

Continuing the example above, suppose that this script is saved in the
current directory into a file called `example.sbatch`. This script
is submitted to the cluster using the following command:

```bash
   $ sbatch ./example.sbatch
```

Many other options are available for submitting jobs using the
`sbatch` command. For more specialized computational needs,
see :ref:`running-jobs`. Additionally, for a complete list of the
available options, see the [Official SBATCH Documentation](https://slurm.schedmd.com/sbatch.html).


### Illustrative sbatch job examples 

Below are a number of example job submission scripts for different types of job use cases.
You can adapt the particular example script that meets your particular use case 
to run your job(s) on MidwayR.

* [Single core/thread jobs](singlecore.md) --  The simplest example (for startup, 1-core job with all default settings)
* [Multithreaded jobs](multithread.md) --  Request multiple threads, (e.g. via OpenMP, etc.)
* [Job arrays](job_arrays.md) -- Submit a group of jobs by one script (job arrays)
* [Parallel software](parallel.md) -- Multiple concurrent tasks in a single job (using "parallel" command)
