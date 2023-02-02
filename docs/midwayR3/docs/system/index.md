# System Overview

MidwayR is comprised of two login nodes and four compute nodes. The total installed storage on MidwayR is 441TB.
It uses Slurm as its workload manger and the software environment module to manage installed software.

**Login Nodes:** MidwayR hosts two login nodes: `sde-login1` and `sde-login2` with the following specifications: 

* CPUs: 2x Intel Xeon Gold 6130 2.1GHz
* Total cores per node: 16 cores
* Threads per core: 2
* Memory: 96GB of RAM

**Compute Nodes:** As of writing this document, MidwayR hosts four compute nodes with the following specifications:

* CPUs: 2x Intel Xeon Gold 6148 2.4GHz
* Total cores per node: 40 cores
* Thread per core: 1
* Memory: 96GB of RAM

**Network:**

* Intel Ethernet Controller 10Gbps Adapter
* Mellanox EDR Infiniband up to 100Gbps bandwidth and a sub-microsecond latency

**File Systems:**

* MidwayR mounts two GPFS filesystems that are shared across all nodes: `/home` and `/project`. Total storage 
for `/home` is 21TB and for `/project` is 420TB.  `/home` has a strict quota of 30GB. Large data should be placed 
on `/project`. MidwayR does not have a scratch filesystem.

**Using MidwayR:**

* MidwayR nodes run CentOS 7.  Its job scheduler is the [Slurm](https://slurm.schedmd.com/). Slurm commands enable 
you to submit, manage, monitor, and control your jobs.

**Software:**

* Organized in [modules](http://modules.sourceforge.net/)
* Use `module avail`, to see what is available
* To load a particular available package, for example, `gcc` version 8.2.0, do `module load gcc/8.2.0`
* If you do not specify a version of the package, the default one is loaded
* To see what environmental variables are modified when `gcc/8.2.0` is loaded, do `module show gcc/8.2.0`
* To unload `gcc/8.2.0`, do `module unload gcc/8.2.0`

**MidwayR Compute Nodes Summary Table:**

| Item                 | Description                          |
| -------------------- | ------------------------------------ |
| Host                 | midwayr.rcc.uchicago.edu             |
| Organization         | RCC                                  |
| Descriptive Name     | RCC Midway Restricted  (MidwayR)     |
| Manufacturer         | Lenovo                               |
| Platform             | ThinkSystem SD530 Linux Cluster      |
| CPU Type             | Intel Xeon Gold 6148                 |
| Operating System     | Linux (CentOS 7.6)                   |
| Total Processor Cores| 160                                  |
| Nodes                | 4                                    |
| Total Memory         | 382GB DDR4-2660 GHz (24GB DIMMs)     |
| Peak Performance     | 3.906 TFlops                         |
| Total Storage        | 441TB                                |
| Interconnect         | 100 Gbps Mellanox EDR Infiniband     |
| Workload Manager     | Slurm                                |
| File System          | GPFS                                 |
| Memory Per CPU       | 2.4GB                                |
| CPU Speed            | 2.4GHz                               |
| CPU Cores Per Node   | 40                                   |
| Memory Per Node      | 96 GB                                |

