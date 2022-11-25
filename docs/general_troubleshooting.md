# General Troubleshooting and Frequently Asked Questions

## Errors in submitting jobs

### Scheduler is busy 

Sometimes when the cluster is being very heavily utilized, the Slurm controller will be busy, and unable to accept your job submission request. If this is happening, you will notice that your job submission commands will hang; you can receive an error message like:

    Unable to allocate resources: Socket timed out on send/recv operation

If this happens, wait a few minutes and try submitting your job again. 

### Error message: Unable to contact Slurm controller


    sbatch: error: Batch job submission failed: Unable to contact Slurm controller (connect failure)

There may be an issue with Slurm. If the error is still seen after a few minutes, report to RCC.

## Jobs that never start

### Requested resources not available
If your jobs requested many cores or a large amount of memory, they may not start running very quickly. You can run squeue -u <userid> -t PD (substitute <userid> with your CNETID) to see the REASON why your jobs are not running. If the REASON seen in squeue is Resources, then the resources you requested in the job submission are not yet available. You may also see the ReqNodeNotAvail job reason if you requested that your job is run on a node that is not available (other jobs are running there, or the node is offline). 

## Jobs that start running and then exit

Jobs can exit for a number of reasons, such as an error in the code, exceeding a time or resource limit you specified, or due to a problem that the node was running on. 
To look up information for a completed job:

    sacct -j <jobid>


### Exceeded run time
If your job runs beyond the "wall clock" time limit you requested with -t in your job submission command, then it will be killed. 

### Exceeded requested memory
If your job uses more memory than you requested using the --mem-per-cpu or --mem parameters in your job submission, it will be killed. You may see errors like this:

    slurmstepd: error: Exceeded job memory limit

or 

    slurmstepd: error: Exceeded step memory limit at some point.

Slurm allows you to have "job steps", which are tasks that are part of a job (See the official Slurm Quick Start Guide for more information). By default, there will be one job step per job. Depending on which memory limit your job exceeds (job limit or step limit), you will see one of the above messages.

# **Slurm Job States**
Your job will report different states before, during, and after execution. The most common ones are seen below, but this is not an exhaustive list. Look at [Job State Codes](https://slurm.schedmd.com/squeue.html#lbAG) in the squeue manual or [this section](https://slurm.schedmd.com/sacct.html#lbAG) in the sacct manual for more detail.

|<p>**Job State**</p><p>***Long form***</p>|<p>**Job State**</p><p>***Short form***</p>|**Meaning**|
| :-: | :-: | :-: |
|CANCELLED|CA|Job was killed, either by the user who submitted it, a system administrator, or for using more resources than requested.|
|COMPLETED|CD|Job has ended in a zero exit status, and all processes from the job are no longer running.|
|COMPLETING|CG|This status differs from COMPLETED because some processes may still be running from this job.|
|FAILED|F|Job did not complete successfully, and ended in a non-zero exit status.|
|NODE\_FAIL|N |The node or nodes that the job was running on had a problem.|
|OUT\_OF\_MEMORY|OOM|The job tried to use more memory than was requested through the scheduler.|
|PENDING|PD|Job is queued, so it is not yet running. Look at the Jobs that never start section for details on why jobs can remain in pending state.|
|RUNNING|R |Job has been allocated resources, and is currently running.|
|TIMEOUT|TO|Job exited because it reached its walltime limit.|
# **Slurm Job Reasons**
If your job is pending, the squeue command will show a "reason" why it is unable to run. Some of these reasons are detailed below, but please reference [Job Reason Codes](https://slurm.schedmd.com/squeue.html#lbAG) in the squeue manual for more detail. 

|**Job Reason**|**Meaning**|
| :-: | :-: |
|AssocMaxCpuPerJobLimit|Job violates accounting/QOS policy (job submit limit, user's size and/or time limits). The job cannot run because the is no allocation in the account.|
|Dependency|The job can't start until a job dependency finishes.|
|JobHeldAdmin |The job will stay pending, as it has been held by an administrator.|
|JobHeldUser|The job will stay pending, as it has been held by the user.|
|NodeDown|A node that the job requires is in "down" state, meaning that the node can't be currently used.|
|Priority|Your job has lower priority than others in the queue. The jobs with higher priority must dispatch first.|
|ReqNodeNotAvail|A node that the job requests using cannot currently accept jobs. ReqNodeNotAvail is a generic reason; in the simplest case, it means that the node is fully in use and is unable to run any more jobs. In other scenarios, this reason can indicate that there is a problem with the node.|
|Resources|The required resources for running this job are not yet available.|

