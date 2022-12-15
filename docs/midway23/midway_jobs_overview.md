# Running Jobs on Midway

This page describes core concepts for running programs on
Midway2 or Midway3. We **highly recommend** reading it in its entirety. 

## Service Units and Allocations  
All jobs running on Midway compute nodes consume
Service Units (SUs), which are aquired through an [allocation](https://rcc.uchicago.edu/accounts-allocations/request-allocation){:target="_blank"}. When you submit a job, you specify the account/allocation to which the SUs will be charged.

Briefly, SUs are a measure of the amount of computing resources (CPUs/GPUs) consumed on a compute cluster. In standard settings, 1 SU equals usage of 1 processing unit for 1 hour, but the exact calculation will vary depending on the amount of memory requested, as well as additional factors like the use of GPUs and CPU architecture. The aim of the Service Unit (SU) is to provide a “fair” account of computing resources. 

Midway2 and Midway3 are compute clusters shared by the entire University of Chicago community. Sharing computational resources creates unique challenges:

1. Jobs must be scheduled in a way that is fair to all users.

2. Consumption of resources needs to be recorded.

3. Access to resources needs to be controlled.

## Slurm Workload Manager

The compute clusters use a **scheduler** to manage requests for
access to compute resources. These requests are called **jobs**, and contain directions about the scripts/programs the user wants to run. In
particular, we use the [Slurm](http://slurm.schedmd.com) workload manager to schedule batch jobs as
well as interactive access to compute nodes.  

You can think of Slurm as the gatekeeper facilitating access the compute nodes. A user on a login node will submit a job to Slurm, which will decide (based on current node utilization and the requested parameters) which nodes to grant the user's job access to.  

Once you have submitted a job via Slurm, there are several commands you may use to [monitor and manage](midway_job_management.md) it.

## Login nodes vs. Compute nodes

Once you have connected to Midway2 or Midway3 (see [Connecting to Midway](midway_connecting.md)) you may work on one of the login nodes. Login nodes may be used for compiling and debugging code, installing software, editing and managing files, submitting jobs, or any other work that is *not* long-running or computationally intensive. *Login nodes should never be used for computionally intensive work.*

All intensive computations should be performed on compute nodes. If you are unsure whether your computations will be intensive, please [request an interactive session](midway_submitting_jobs.md#interactive-jobs) and continue your work once you have connected to the compute node. There are multiple types of compute nodes, organized into [partitions](#partitions).

**WARNING**: Running computationally intensive jobs on the login nodes prevents other users from efficiently using the cluster. RCC System Administrators may terminate your processes without warning if your processes disrupt other users’ work on the RCC cluster.  

## Interactive vs. Batch Jobs  
There are two main ways to run programs on Midway: Interactively, via an "interactive job", and non-interactively, via a "batch job".  

**Key point:** *In an interactive session, you will load [software modules](/midway23/software/midway_software_overview) and run your scripts in real-time, whereas when submitting batch jobs, you specify the software modules to be loaded and scripts to be run in advance.*

Interactive jobs are the most intutive way to use Midway, as they allow you to interact with the program running on compute node/s (e.g., execute cells in a Jupyter Notebook) in real-time. This is great for exploratory work or troubleshooting. An interactive job will persist until you disconnect from the compute node, or until you reach the maximum requested time. *

Batch jobs are non-interactive, as you submit a script to be executed on a compute node with no possibility of interactivity. A batch job doesn't require you to be logged in after submission, and ends when either (1) the script is finished running, (2) job's maximum time is reached, or (3) an error occurs.  

The next page, [Submitting Jobs](midway_submitting_jobs.md), will show you how to initiate both types of jobs.

## Partitions
Midway compute nodes are organized into "partitions", subsets of nodes typically grouped by their hardware or ownership. When submitting a job you specify the partition it will run on by setting the `--partition=<partition>` flag. To view all partitions and node information, enter the command:
```
rcchelp sinfo
```  

This table summarizes the available communal partitions: 

=== "Midway2"

    | Partition | Description |  Num. of Nodes | Node Specifications* |  
    | ----------- | ----------- |  ----------- | ----------- |
    | `broadwl` | Default (CPU) partition; the choice for most jobs | ? | 64 GB Memory, ? GB SSD |
    | `gpu2` | GPU partition (4 cards per node); for ML or other GPU-accelerated jobs | 6 | GPU nodes with 4x NVIDIA K80 cards per node  | 
    | `bigmem2` | Small partition with large amounts of memory per node; for jobs requiring large amounts of memory | 5 | ? |

    *Every node has ? Intel Broadwell CPUs (28 cores), ? GB of local SSD storage, and a 100 Gbps HDR InfiniBand network card. 

=== "Midway3"

    | Partition | Description | Num. of Nodes | Node Specifications* |  
    | ----------- | ----------- | ----------- |  ----------- |  
    | `caslake`| Default (CPU) partition; the choice for most jobs| 214 | 192 GB Memory |
    | `gpu` | GPU partition (4 cards per node); for ML or other GPU-accelerated jobs | 11 | Either NVIDIA V100, RTX 6000, or A100 cards | 
    | `bigmem` | Small partition with large amounts of memory per node; for jobs requiring large amounts of memory |  2 | 768 GB and 1.52 TB Memory | 
    | `amd` | CPU partition with AMD processors | 36 | AMD EPYC Rome CPU (2x per node) | 

    *Every node (except those in the `amd` partition) has 2 Intel Cascade Lake 6248R CPUs (48 cores), 900 GB of local SSD storage, and a 100 Gbps HDR InfiniBand network card.

## Job Limits and QOS
To distribute computational resources fairly the RCC sets limits on the amount of computing resources that may be requested by a single user at any given time. These limits are enforced by the QOS (Quality of Service) assigned to each partition. A QOS is essentially a set of parameters, and each partition has its own, summarized in this table:

=== "Midway2"

    | QOS | Max CPUs Per User | Max Nodes Per User | Max Jobs Per User|  Max Wall Time | 
    | ----------- | ----------- |  ----------- |  ----------- | ----------- |
    | `broadwl` | 2800 | 100 | 100 | 36 H |
    | `gpu2` | ? | ? | 10 | 36 H | 
    | `bigmem2` | 112 | ? | 5 | 36 H |

=== "Midway3"

    | QOS | Max CPUs Per User | Max Nodes Per User | Max Jobs Per User|  Max Wall Time | 
    | ----------- | ----------- |  ----------- |  ----------- | ----------- |
    | `caslake` | 100 | 4800 | 1000 | 36 H |
    | `gpu` | 192 | 4 | 12 | 36 H | 
    | `bigmem` | 96 | ? | 10 | 36 H |
    | `amd` | 1024 | 8 | 20 | 36 H |

Groups participating in the cluster parternership program may customize resources limits for their partitions.

Additional information on limits can be found by entering the command 
```
rcchelp qos
``` 
on any login or compute node on Midway2 or Midway3.

Observe that these limits are often different depending on the partition.

If your research requires a temporary exception to a particular limit, you may apply for a special allocation. Special allocations are evaluated on an individual basis and may or may not be granted.
