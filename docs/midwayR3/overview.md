# Welcome to MidwayR3 user guide

MidwayR3 is the RCC's secure cluster that provides a secure computing environment to support research with higher security standard requirements. If you have any questions about MidwayR3, please email midwayr@rcc.uchicago.edu.

# System Overview

MidwayR is comprised of two login nodes and four compute nodes. The total installed storage on MidwayR is 441TB. It uses SLURM as its workload manager and the software environment module to manage installed software.
<br><br/>
**Login Nodes:** MidwayR3 hosts login nodes with the following specifications: 

* CPUs: 2x Intel Xeon Gold 6130 2.1GHz
* Total cores per node: 16 cores
* Threads per core: 2
* Memory: 96GB of RAM

**Compute Nodes:** 
See [Partitions](../partitions/index.md)

**Network:**

* Intel Ethernet Controller 10Gbps Adapter
* Mellanox EDR Infiniband up to 100Gbps bandwidth and a sub-microsecond latency

**File Systems:**

* MidwayR mounts two GPFS filesystems that are shared across all nodes: `/home` and `/project`. Total storage 
for `/home` is 21TB and for `/project` is 420TB.  `/home` has a strict quota of 30GB. Large data should be placed 
on `/project`. MidwayR does not have a scratch filesystem.

**Using MidwayR3:**

* MidwayR nodes run CentOS 7.  Its job scheduler is the [SLURM](https://slurm.schedmd.com/). Slurm commands enable you to submit, manage, monitor, and control your jobs.

**Software:**

* Organized in [modules](http://modules.sourceforge.net/)
* Use `module avail`, to see what is available
* To load a particular available package, for example, `gcc` version 8.2.0, do `module load gcc/8.2.0`
* If you do not specify a version of the package, the default one is loaded
* To see what environmental variables are modified when `gcc/8.2.0` is loaded, do `module show gcc/8.2.0`
* To unload `gcc/8.2.0`, do `module unload gcc/8.2.0`



