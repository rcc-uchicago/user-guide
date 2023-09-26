# Running jobs on RCC clusters

This page describes core concepts for running programs on RCC clusters. 

## Service units, allocations, and accounts 
All jobs running on RCC clusters compute nodes consume service units (SUs). In short, SUs measure the amount of computing resources (CPUs/GPUs/time) consumed on a compute cluster. 

!!! info "More information on SUs"
    In standard settings, 1 SU equals the usage of 1 processing unit for 1 hour, but the exact calculation will vary depending on the amount of memory requested, as well as additional factors like the use of GPUs and CPU architecture. By using SUs, we aim to provide “fair” access to computing resources.

SUs can be requested through an [allocation](https://rcc.uchicago.edu/accounts-allocations/request-allocation). Allocations are ultimately associated with a PI's account. Thus, when we submit a job, we specify the account to which the SUs will be charged. If we submit a job on Midway2 without specifying an account, your default account (likely `pi-drpepper`) will be used. On Midway3 **you must** specify an account for a job to be successfully submitted. 
    
## Slurm workload manager

RCC's shared clusters (Midway2, Midway3, etc.) are compute clusters shared with the entire RCC user community. To keep track of the usage of this sharing computational resources:

1. Jobs must be scheduled in a way that is fair to all users. 

2. Consumption of resources needs to be recorded. 

3. Access to resources needs to be controlled. 

Consequently, the compute clusters use a **scheduler** to queue the requests for access to compute resources. These requests are called **jobs** and contain directions about the scripts/programs the user wants to run. In particular, we use the [Slurm](http://slurm.schedmd.com) workload manager to schedule jobs in batch and interactive formats.  

You can think of Slurm as the queue manager that facilitates access to the compute nodes. We submit a job to Slurm, which decides (based on current node utilization and the requested parameters) which compute nodes are permitted to use and available to send your job to. 

# Submitting Jobs
The flowchart below illustrates the main steps in that process. 

<p align="center">
<img src="../img/slurm/slurm_fig_000.png" width="640" />
</p> 

### Interactive (active) vs. batch (passive) jobs  
There are two main ways to run programs on RCC clusters: 

* Active via an "interactive session"; 

* Passive via a "batch job" 

In an interactive session, you will load [software modules](software/software-overview.md) and run your scripts in real-time, whereas when submitting batch jobs, you specify the software modules to be loaded and scripts to be run in advance. 

Interactive jobs allow you to actively interact with the program running on compute node/s (e.g., execute cells in a Jupyter Notebook) in real-time. This is great for exploratory work or troubleshooting. An interactive job will persist until you disconnect from the compute node or until you reach the maximum requested time. 

Batch jobs are non-interactive, as you submit a script to be executed on a compute node with no possibility of interactivity. A batch job doesn't require you to be logged in after submission and ends when either (1) the script is finished running, (2) the job's maximum time is reached, or (3) an error occurs. 

* [Running jobs on RCC compute nodes through `sinteractive` (active) ](slurm-sinteractive.md)
* [Submitting jobs to RCC compute nodes through `sbatch` (passive) ](slurm-sbatch.md)


## Job limits and QoS
To distribute computational resources fairly, the RCC limits the computing resources users request. These limits are enforced by the QoS (Quality of Service) assigned to each partition. A QoS is a set of parameters (e.g., MaxNodes, MaxCPUs, MaxWall, etc.) Read more about these regulations on our [partitions](partitions.md#shared-partition-qos) page. 

Groups participating in the cluster partnership program (CPP) may customize resource limits for their partitions. 

Additional information on limits can be found by entering the command:  
```
rcchelp qos
``` 
Observe that QoS are often different depending on the partition.

You can request temporary exceptions to a particular limit by contacting our [helpdesk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support). Special allocations are evaluated on an individual basis and may or may not be granted. 
