# Welcome to MidwayR3 user guide

MidwayR3 (also known as MidwayR) is the RCC's secure HPC cluster that provides a trusted research environment to support work with regulated research data that requires high-level protection. 

Examples of regulated research data include:

* Personally Identifiable Information (PII)
* Limited data sets as per Health Insurance Portability and Accountability Act (HIPAA) definition
* Some Types of Health Information 
* Data covered under the Federal Information Security Management Act (FISMA)
* Data covered under the Federal Education Rights and Privacy Act (FERPA)
* Data with security requirements set by the Institutional Review Board (IRB)
* Commercial data with security requirements set by the Data Use Agreement (DUA)

The [research data classification](https://srds.uchicago.edu/secure-research-data-usage-guide/) is provided by University Research Administration. If you have any questions about MidwayR3, please email midwayr-help@rcc.uchicago.edu.

# System Overview

MidwayR3 is comprised of two login nodes and four compute nodes. The total installed storage on MidwayR3 is 441TB. It uses SLURM as its workload manager and the software environment module system to manage installed software.
<br><br/>
**Login Nodes:** MidwayR3 hosts login nodes with the following specifications: 

* CPUs: 2x Intel Xeon Gold 6130 2.1GHz
* Total cores per node: 16 cores
* Threads per core: 2
* Memory: 96GB of RAM

**Compute Nodes:** 
There are no limits on SU usage at the moment. PIs don't need to apply for SUs allocation.
See [Partitions](partitions.md)

**Network:**

* Intel Ethernet Controller 10Gbps Adapter
* Mellanox EDR Infiniband up to 100Gbps bandwidth and a sub-microsecond latency
* Neither compute nor login nodes have direct access to the Internet

**File Systems:**

* MidwayR3 utilizes a GPFS filesystem, with `/home` and `/project` directories mounted for private and collaborative work. 
The `/home/<CNetID>` directory has a strict quota of 30GB and the quota for `/project/pi-<PI_CNETID>-<ProjectName>` varies depending on the project with the default startup storage allocation of 500 GB. MidwayR3 does not have a scratch filesystem.
<!-- Total cumulative storage for `/home` is 21TB and for `/project` is 420TB.   -->

**Using MidwayR3:**

* MidwayR3 nodes run CentOS 7. Its job scheduler is the [SLURM](https://slurm.schedmd.com/). Slurm commands enable you to submit, manage, monitor, and control your jobs.

**Software:**

* Organized in [modules](http://modules.sourceforge.net/)
* Use `module avail`, to see what is available
* To load a particular available package, for example, `gcc` version 8.2.0, do `module load gcc/8.2.0`
* If you do not specify a version of the package, the default one is loaded
* To see what environmental variables are modified when `gcc/8.2.0` is loaded, do `module show gcc/8.2.0`
* To unload `gcc/8.2.0`, do `module unload gcc/8.2.0`



