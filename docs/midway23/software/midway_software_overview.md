# Software

This page contains software-specific information.  For more general
information on how to run different types of jobs on Midway2, consult
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

When you first log into Midway, you will be entered into a very
'bare-bones' user environment with minimal software available.  The
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

For more information on how to use software modules on Midway2, consult [Using software modules on Midway](../tutorials/intro-to-software-modules/index.md#intro-to-software-modules).

## Full Software Module List

The best way to view the most current software offerings of RCC is to check the list of available software modules with the `module avail` command on Midway2.  You may also view the complete [Software Module List](modules/index.md#modules) online.
