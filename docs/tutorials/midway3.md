# Introduction

This tutorial shows the basic steps to use the Midway3 cluster at the RCC.  For complete RCC technical documentation, see the main sections of this user guide.

## Logging into the Midway3 login node

For the complete documentation regarding connecting to RCC resources see: [Connecting to Midway](../101/connecting.md). Here you will use [Secure Shell (SSH)](../ssh/main.md) to connect to the login node from your local machine.

```
ssh [your-cnetid]@midway3.rcc.uchicago.edu
```

After putting in your password, you will choose an option to accept a push on the Duo app. If successful, you will land on your home folder on the Midway3 login node as shown at the command prompt `[your-cnetid]@midway3-login3` or `[your-cnetid]@midway3-login4`.

You can check where the present working directory by running the command `pwd`:

```
pwd
```

##  Getting your software ready

You should check what software packages are already installed on Midway3 via `module avail` and `module list`. Many commonly used software packages and libraries have been installed on Midway for your use.  For an overview of how to use Software Modules on Midway, consult the RCC [Software](../software/index.md) documentation page.

For this tutorial, let us load `python`

```
module load python
```

which will load the default version of the `python/anaconda` module. You can do `module list` to see which version is just loaded.

Suppose that you would like to install numpy, matplotlib and pandas for your calculations.  You should first create an environment in your own space and install these packages into this environment.  See [managing Python environments](../software/apps-and-envs/python.md) for more information.

Since Python environments might contain many files and/or take a lot space, it is recommended that you create your environments somewhere outside your home folder such as `/project` or `/scratch`. Suppose that your PI has a space under `/project/[pi-folder]` and you have a folder under that location.

```
cd /project/[pi-folder]/[your-cnetid]
python -m venv my-venv
source activate ./my-venv
pip install matplotlib numpy pandas
```

Note that the base environment of the default `python` module already has many popular packages installed, including the above 3 packages. You can also create an environment and install packages with `conda` or `mamba`.

If you need to compile your software packages from source, you can download the software source code from GitHub to your space, load the compiler modules and build the codes. In this tutorial, let us build [LAMMPS](https://github.com/lammps/lammps) from source code:

```
cd /project/[pi-folder]/[your-cnetid]
git clone https://github.com/lammps/lammps.git
cd lammps
mkdir build && cd build
```

Load the modules for the preferred compiler, MPI libraries and MKL, and cmake to configure the build:
```
module load mpich/3.4.3+gcc-10.2.0 mkl/2023.1 cmake/3.26
cmake ../cmake -C ../cmake/presets/basic.cmake -DFFT=MKL -DFFTW3_INCLUDE_DIR=$MKLROOT/include/fftw
```

and finally build the code

```
make -j4
```

If the build succeeds, you will see a LAMMPS binary, namely `lmp`, generated under the folder `/project/[pi-folder]/[your-cnetid]/build`.

You can use other compilers (Intel oneAPI, GNU GCC) and MPI libraries (OpenMPI, MPICH). For GPU codes, you can use NVIDIA HPC SDK and Intel oneAPI. More information on the available development tools is given in [Compilers](../software/compilers.md).

## Getting your data ready

idway3 compute nodes have access to `/project` and `/project2`, in addition to the shared scratch space `/scratch/midway3`. It is recommended that you put your input and output data under one of those spaces for fast access from the compute nodes. See [Storage](../storage/main.md) for more details.

```
cd /project/[pi-folder]/[your-cnetid]
git clone https://github.com/[some-data-pool.git]
```
or
```
wget [some-url]
```

In this tutorial, let us say we have the input data in the `examples` folder in the `lammps` repo from above.

## Running jobs on the compute nodes

See [Running Jobs on Midway](../slurm/main.md) for detailed documentation on how to run your own programs on the cluster once you've connected. In this tutorial, we will try interactive session and submit a batch job.

Before running any job, you need to check if your account has any eligible allocations:

```
rcchelp balance
```

If you don't have any PI account, or if the balance column has negative numbers, then you cannot run any jobs on the shared partitions on Midway3. More on allocations can be found at [Allocations](../101/allocations.md).

### Interactive session

On the Midway3 login node, request an interactive node with 8 CPU cores:

```
sinteractive -A [pi-account] -p caslake -N 1 --ntasks-per-node=8
```

which will take a while to get you a compute node. This is because the `sinteractive` command essentially invokes the Slurm command `salloc` with the requested resource, and waits for the Slurm manager to return the resource. If successful, you will see an empty screen with the command prompt `[your-cnetid]@midway3-0xyz`, indicating that you are on the compute node node `midway3-0xyz`.

You can load python as you did on the login node:
```
module load python
```

and run `python`

```
[your-cnetid@midway3-0xyz ] python
Python 3.9.19 | packaged by conda-forge | (main, Mar 20 2024, 12:50:21) 
[GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

After quitting `python`, you can activate the environment you created, and list the installed packages

```
source /project/[pi-folder]/[your-cnetid]/my-venv/bin/activate
pip list
```
You should see `numpy`, `matplotlib` and `pandas` installed in this environment.

Let us prepare a simple Python script, namely, `simple.py` with a text editor like `nano`, in the current folder, with the following content:

```
import numpy as np
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y)
plt.savefig("output.pdf", format="pdf")
```
And run it with 

```
python simple.py
```

which should produce a file `output.pdf`.

Change to the input data folder
```
cd /project/[pi-folder]/[your-cnetid]/lammps/examples
```

Load the same modules you used to build LAMMPS (except `cmake`)

```
module load mpich/3.4.3+gcc-10.2.0 mkl/2023.1
```

Relax the locked memory limit
```
ulimit -l unlimited
```

Run the LAMMPS binary you built above
```
mpirun -np 8 /project/[pi-folder]/[your-cnetid]/lammps/build/lmp -in melt/in.melt
```

The run will produce the LAMMPS screen output and a file named `log.lammps` in the current folder.

To terminate the interactive session, run

```
exit
```

You will get back to the login node.

### Batch jobs

Next, let us run the same calculations in the batch mode. First, create a text file with `nano` or `vi` on the login node, namely, `batch_job_python.txt`

```
#!/bin/bash
#SBATCH --job-name=job-info
#SBATCH --account=[pi-account]
#SBATCH --partition=caslake
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

cd /project/[pi-folder]/[your-cnetid]/
source my-venv/bin/activate
python simple.py
```

Next, submit the job to Slurm
```
sbatch batch_job_python.txt
```

Check your submitted job in the queue with

```
squeue -u $USER
```

Next, to test a run with LAMMPS in the batch mode, create another text file with `nano` or `vi` on the login node, namely, `batch_job_lammps.txt`

```
#!/bin/bash
#SBATCH --job-name=job-info
#SBATCH --account=[pi-account]
#SBATCH --partition=caslake
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8

cd /project/[pi-folder]/[your-cnetid]/lammps/examples
module load mpich/3.4.3+gcc-10.2.0 mkl/2023.1
ulimit -l unlimited

n=$(( SLURM_NNODES * SLURM_NTASKS_PER_NODE ))

mpirun -np $n /project/[pi-folder]/[your-cnetid]/lammps/build/lmp -in melt/in.melt
```

After saving the file (Ctrl+X with `nano`, `:x` with `vi`), you will submit the script to Slurm:

```
sbatch batch_job_lammps.txt
```

As you can see, you can submit more than one jobs at a time. The more resource you request (number of nodes, number of tasks per node, memory per node, walltime and so on), the longer the jobs are pending.  Your usage history also affects how soon your jobs get running.  See [Running Jobs on Midway](../slurm/main.md) for detailed documentation on how to monitor the submitted jobs.

You can check the generated output `output.pdf` and `log.lammps` in the corresponding directories.

# Summary

In this tutorial, you have learned how to log in to Midway3, build your codes and/or load installed software packages, prepare input data and job scripts, and submit jobs to Slurm.

# Getting Help

RCC support staff is available to assist with technical issues (help logging in, questions about using the cluster, etc).  Please don’t hesitate to ask questions if you encounter any technical issues.

* The preferred way of requesting support is to [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target='_blank'}.

* RCC’s walk-in lab is open during business hours and is located in Regenstein Library room 216. Feel free to drop by to chat with one of our staff members if you get stuck.

