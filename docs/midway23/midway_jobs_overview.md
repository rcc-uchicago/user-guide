# Running Jobs on Midway

This page describes core concepts for running programs on
Midway2 or Midway3. We **highly recommend** reading it in its entirety. 

## Service Units, Allocations, and Accounts  
All jobs running on Midway compute nodes consume Service Units (SUs). In short, SUs are a measure of the amount of computing resources (CPUs/GPUs) consumed on a compute cluster. 

??? info
    In standard settings, 1 SU equals usage of 1 processing unit for 1 hour, but the exact calculation will vary depending on the amount of memory requested, as well as additional factors like the use of GPUs and CPU architecture. The aim of the Service Unit (SU) is to provide a “fair” account of computing resources.

SUs are aquired through an [allocation](https://rcc.uchicago.edu/accounts-allocations/request-allocation){:target="_blank"}. Allocations are ultimately associated with Midway *accounts*, thus when you submit a job, you specify the account to which the SUs will be charged. If you submit a job on Midway2 without specifying an account, your default account (likely `pi-<PI CNetID>`) will be used. On Midway3 **you must** specify an account for a job to be successfully submitted.
    
## Slurm Workload Manager

Midway2 and Midway3 are compute clusters shared by the entire University of Chicago community. Sharing computational resources creates unique challenges:

1. Jobs must be scheduled in a way that is fair to all users.

2. Consumption of resources needs to be recorded.

3. Access to resources needs to be controlled.


Consequently, the compute clusters use a **scheduler** to manage requests for
access to compute resources. These requests are called **jobs**, and contain directions about the scripts/programs the user wants to run. In
particular, we use the [Slurm](http://slurm.schedmd.com) workload manager to schedule batch jobs as
well as interactive access to compute nodes.  

You can think of Slurm as the gatekeeper facilitating access the compute nodes. A user on a login node will submit a job to Slurm, which will decide (based on current node utilization and the requested parameters) which nodes to grant the user's job access to.  

Once you have submitted a job via Slurm, there are several commands you may use to [monitor and manage](midway_job_management.md) it.

## Login nodes vs. Compute nodes

Once you have connected to Midway2 or Midway3 (see [Connecting to Midway](midway_connecting.md)), you may work on one of the login nodes. Login nodes may be used for compiling and debugging code, installing software, editing and managing files, submitting jobs, or any other work that is *not* long-running or computationally intensive. *Login nodes should never be used for computionally intensive work.*

All intensive computations should be performed on compute nodes. If you are unsure whether your computations will be intensive, please [request an interactive session](midway_submitting_jobs.md#interactive-jobs) and continue your work once you have connected to the compute node.

???+ warning
    Running computationally intensive jobs on the login nodes prevents other users from efficiently using the cluster. RCC System Administrators may terminate your processes without warning if your processes disrupt other users’ work on the RCC cluster.  

## Interactive vs. Batch Jobs  
There are two main ways to run programs on Midway: Interactively, via an "interactive job", and non-interactively, via a "batch job".  

**In short**, in an interactive session, you will load [software modules](/midway23/software/midway_software_overview) and run your scripts in real-time, whereas when submitting batch jobs, you specify the software modules to be loaded and scripts to be run in advance.

Interactive jobs allow you to interact with the program running on compute node/s (e.g., execute cells in a Jupyter Notebook) in real-time. This is great for exploratory work or troubleshooting. An interactive job will persist until you disconnect from the compute node, or until you reach the maximum requested time. *

Batch jobs are non-interactive, as you submit a script to be executed on a compute node with no possibility of interactivity. A batch job doesn't require you to be logged in after submission, and ends when either (1) the script is finished running, (2) job's maximum time is reached, or (3) an error occurs.  

The next page, [Submitting Jobs](midway_submitting_jobs.md), will show you how to initiate both types of jobs.

## Partitions
Midway compute nodes are organized into "partitions", subsets of nodes typically grouped by their hardware or ownership. When submitting a job via Slurm, you specify the partition it will run on by setting the `--partition=<partition>` flag. Most users will submit jobs to a 'shared' partition--a partition accessible to all Midway users.  

See the [Partitions page](midway_partitions.md) for information about all of the Midway partitions.



## Job Limits and QOS
To distribute computational resources fairly the RCC sets limits on the amount of computing resources that may be requested by a single user at any given time. These limits are enforced by the QOS (Quality of Service) assigned to each partition. A QOS is essentially a set of parameters, and each partition has its own, summarized in this table:

=== "Midway2"

    | QOS | Max CPUs Per User | Max Nodes Per User | Max Jobs Per User|  Max Wall Time | 
    | ----------- | ----------- |  ----------- |  ----------- | ----------- |
    | `broadwl` | 2800 | 100 | 100 | 36 H |
    | `gpu2` | ? | ? | 10 | 36 H | 
    | `bigmem2` | 112 | ? | 5 | 36 H |

===+ "Midway3"

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
