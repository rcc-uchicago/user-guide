# Software

This page contains information about software on Midway.  For more general
information on how to run different types of jobs on Midway, consult
[Running Jobs](/midway23/midway_jobs_overview).

RCC has a large selection of software available, but if you need
software not currently available in the module system, send a detailed
request to [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu).

## Using Software Modules

RCC uses [Environment Modules](http://modules.sourceforge.net) for
managing software. The modules system permits us to set up the shell
environment to make running and compiling software easier. It also
allows us to make available many software packages and libraries that
would otherwise conflict with one another.

When you first log into Midway, you will be entered into a 
basic user environment with minimal software available.  The
`module` system is a script based system used to manage the user
environment and to “activate” software packages.  In order to access
software that is installed on Midway, you must first load the
corresponding software module.

Basic `module` commands:

| Command  | Description | 
| --------- | --------- | 
| `module avail`          |   lists all available software modules            |    
| `module avail [name]`   |   lists modules matching [name]                   |
| `module load [name]`    |   loads the named module                          |
| `module unload [name]`  |   unloads the named module                        |
| `module list`           |   lists the modules currently loaded for the user |

## Commonly Used Applications

This guide contains instructions for some commonly used applications and environments including:

* [Python and Jupyter Notebook](../software/apps_and_envs/python.md)  
* [R](../software/apps_and_envs/r.md)  
* [MATLAB](../software/apps_and_envs/matlab.md)    
* [Stata](../software/apps_and_envs/stata.md)    
* [Mathematica](../software/apps_and_envs/mathematica.md)  
* [Perl](../software/apps_and_envs/perl.md)  
* [Spark](../software/apps_and_envs/spark.md)  
* [Tensorflow and PyTorch](../software/apps_and_envs/tf_and_torch.md)  
* [GROMACS](../software/apps_and_envs/gromacs.md)  
* [LAMMPS](../software/apps_and_envs/lammps.md)  
* [NAMD](../software/apps_and_envs/namd.md)  

## Full Software Module List

The best way to view the most current software offerings of RCC is to check the list of available software modules with the `module avail` command on Midway.

