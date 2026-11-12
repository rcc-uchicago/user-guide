# MATLAB

RCC provides the MATLAB programming environment on all Midway compute resources. Most MATLAB toolboxes are also available (see [https://itservices.uchicago.edu/page/matlab-tah-toolboxes](https://itservices.uchicago.edu/page/matlab-tah-toolboxes)). When running compute- or memory-intensive MATLAB jobs on Midway, it is important to run them on compute nodes, not on the login nodes.

!!! note
    Compute- and memory-intensive jobs running on the login nodes are subject to termination without warning by RCC system administrators, as they impact the performance of the login nodes and the ability of other users to work.

## Getting Started

To gain access to MATLAB, a MATLAB module must be loaded with the command:

```bash
module load matlab
```

A full list of the available MATLAB versions can be obtained by issuing the command:

```bash
module avail matlab
```

## Using MATLAB’s Textual Interface

On Midway, MATLAB can be launched at the terminal with the commands:

```bash
module load matlab
matlab
```

This will launch MATLAB’s textual interface. We recommend running MATLAB on a compute node as opposed to a login node. 

## Using MATLAB’s Graphical Interface

To use MATLAB’s GUI on Midway, we recommend connecting to Midway via [ThinLinc](../../connection/thinlinc/main.md). 

Note that once connected via ThinLinc, you will be accessing a Midway login node. To run MATLAB with its GUI on a compute node, open a terminal in the ThinLinc desktop and issue the [`sinteractive`](../../slurm/sinteractive.md) command. This will take you to a compute node.  From there, you can launch MATLAB with the command:

```bash
module load matlab
matlab
```

and have access to the GUI.

## Running MATLAB Jobs with Slurm

To submit MATLAB jobs to Midway’s resource scheduler, Slurm, the MATLAB commands to be executed must be contained in a single `.m` script.

For example, suppose `matlab_simple.m` is a basic MATLAB script that computes and prints a 10x10 magic square, and `matlab_simple.sbatch` is a submission script that runs the MATLAB program on the default partition.

Place both files in a directory on Midway. Then, enter the following command to submit the program `matlab_simple.m` to the scheduler:

```bash
sbatch matlab_simple.sbatch
```

Output from this example can be found in the file named `matlab.out`, which will be created in the same directory.

## MATLAB Parallel

Running MATLAB effectively with parallel computing techniques requires a few
basic concepts, which can be optimized and expanded upon. The MATLAB Parallel
Computing Toolbox User’s Guide is the official documentation and should be
referred to for further details, examples, and explanations.  Here, we provide
some Midway-specific considerations that RCC users should be aware of.

RCC recommends MATLAB 2014b or later for parallel MATLAB computing, as it relaxes the restriction on the number of workers available through the PCT.

**NOTE**: At this time, RCC does not support the MATLAB Distributed Computing Server (MDCS). As such, parallel MATLAB jobs are limited to a single node with the “local” pool through use of the Parallel Computing Toolbox (PCT). 

### Basic PCT Operation

The most basic level of parallelization in MATLAB is achieved through use of a `parfor` loop in place of a `for` loop. The iterations of a `parfor` loop are distributed to the workers in the active pool and computed concurrently. For this reason, care must be taken to ensure that each iteration of the `parfor` loop is independent of every other.

The overall procedure for leveraging `parfor` in your MATLAB script is as follows:


1. Create a local parallel pool


2. Call `parfor` in place of `for` in your MATLAB scripts and functions

A simple MATLAB script that uses `parfor`, `matlab_parfor.m`, is shown below.

```matlab
% start the matlabpool with maximum available workers
% control how many workers by setting ntasks in your sbatch script
pc = parcluster('local')
parpool(pc, str2num(getenv('SLURM_CPUS_ON_NODE')))

% run a parfor loop, distributing the iterations to the SLURM_CPUS_ON_NODE workers
parfor i = 1:100

        ones(10,10)

end
```

### Submitting a PCT MATLAB Job to Slurm

Compute-intensive jobs that consume non-trivial amounts of CPU and/or memory resources should not be run on Midway’s login nodes. Instead, the job should be submitted to the scheduler and run on a compute node. A sample submission script for the above MATLAB example, `matlab_parfor.sbatch`, is shown below.

```bash
#!/bin/bash

#SBATCH --job-name=whatever
#SBATCH --output=matlab_parfor.out
#SBATCH --error=matlab_parfor.err
#SBATCH --partition=caslake
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=16

module load matlab/2014b

matlab -nodisplay < matlab_parfor.m

```

### Running Multiple PCT MATLAB Jobs

Specific care must be taken when running multiple PCT jobs on Midway. When you submit multiple jobs that all use PCT for parallelization, the parallel pools that get created can interfere with one another, which can lead to errors and early termination of your scripts.

The MATLAB PCT requires a temporary “Job Storage Location” where it stores information about the MATLAB pool that is in use. This is simply a directory on the filesystem that MATLAB writes various files to in order to coordinate the parallelization of the pool. By default, this information is stored in `/home/YourUsername/.matlab/` (the default “Job Storage Location”). When you submit multiple jobs to Slurm that all use the PCT, all of the jobs will attempt to use this default location for storing job information, creating a race condition where one job modifies the files that were put in place by another. Clearly, this situation must be avoided.

The solution is to have each of your jobs that use the PCT set a unique location for storing job information. To do this, a temporary directory must be created before launching MATLAB in your submission script, and then the pool must be created to explicitly use this unique temporary directory.  An example sbatch script `matlab_multi.sbatch` to do this is shown below:

```bash
#!/bin/bash

#SBATCH --job-name=whatever
#SBATCH --output=matlab_parfor.out
#SBATCH --error=matlab_parfor.err
#SBATCH --partition=caslake
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=16

module load matlab/2014b

# Create a temporary directory on scratch
mkdir -p $SCRATCH/$SLURM_JOB_ID

# Kick off matlab
matlab -nodisplay < multi_parfor.m 

# Cleanup local work directory
rm -rf $SCRATCH/$SLURM_JOB_ID

```

And the corresponding MATLAB script `multi_parfor.m` is shown here:

```matlab


% create a local cluster object
pc = parcluster('local')

% explicitly set the JobStorageLocation to the temp directory that was created in your sbatch script
pc.JobStorageLocation = strcat(getenv('SCRATCH'),'/', getenv('SLURM_JOB_ID'))

% start the matlabpool with maximum available workers
% control how many workers by setting ntasks in your sbatch script
parpool(pc, str2num(getenv('SLURM_CPUS_ON_NODE')))

% run a parallel for loop
parfor i = 1:100
    ones(10,10)
end
```
