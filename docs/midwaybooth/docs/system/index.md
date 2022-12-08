# System Overview

MidwayBooth is composed of 21 decicated compute nodes within the Midway high-performance ecosystem. MidwayBooth features Intel Cascade Lake nodes, HDR InfiniBand interconnect, and SSD storage controllers for more performant small file I/O. The total installed storage on MidwayBooth is 400TB, whereby 100TB is reserved for the secure data enclave, MidwayR.
The cluster uses Slurm as its workload manger and the software environment module to manage installed software.

**Intel Hardware Key Features:** MidwayBooth hosts three login nodes: `midwaybooth-login1`, `midwaybooth-login2` and `midwaybooth-login3`as well as 18 compute nodes 

* CPUs: 21 nodes total 
* All nodes have HDR InfiniBand (100 Gbps) network cards
* Each node has 960 GB SSD local disk
* Operating System throughout cluster is CentOS 8

**File Systems:**

* There is a total of 300TB of raw parallel file storage that is part of the MidwayBooth cluster. The new storage system is designed such that any file smaller than 4KB in size is bundled with the file metadata and stored on the pool of dedicated metadata SSDs that are part of the parallel storage system. This can lead to considerable improvement in performance for small file size (<4KB) I/O. This feature was not available with Midway2, where the metadata and data were stored on slower mechanical hard drives. 

**Using MidwayBooth:**

* MidwayBooth nodes run CentOS 8.  Its job scheduler is the [Slurm](https://slurm.schedmd.com/). Slurm commands enable you to submit, manage, monitor, and control your jobs.

**Software:**

* If using ThinLinc, available software is visible as icons on the desktop.
* Organized in [modules](http://modules.sourceforge.net/)
* Use `module avail`, to see what is available
* To load a particular available package, for example, `gcc` version 8.2.0, do `module load gcc/8.2.0`
* If you do not specify a version of the package, the default one is loaded
* To see what environmental variables are modified when `gcc/8.2.0` is loaded, do `module show gcc/8.2.0`
* To unload `gcc/8.2.0`, do `module unload gcc/8.2.0`

**Definition of Terms:**

* When reading the User Guide, please keep in mind the following:
* - A core is the basic computational unit of a multiprocessor CPU.
* - A node is a single machine with memory, cores, operating system and network connection.
* - A partition is a collection of nodes with similar technical specifications (memory, cores, etc.)
* - The cluster is the complete collection of nodes with networking and file storage facilities.
