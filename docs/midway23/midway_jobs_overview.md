# Running jobs on midway

The information here describes how users can run computations on
Midway 2 or Midway 3. All jobs running on compute nodes consume
Service Units (SUs); see RCC Service Units (link) for more information.

Midway 2 and Midway 3 are compute clusters shared by the entire University of Chicago community. Sharing computational resources creates unique challenges:

1. Jobs must be scheduled in a way that is fair to all users.

2. Consumption of resources needs to be recorded.

3. Access to resources needs to be controlled.

The compute clusters use a **scheduler** to manage requests for
access to compute resources. These requests are called **jobs**. In
particular, we use the [Slurm](http://slurm.schedmd.com) resource manager to schedule jobs as
well as interactive access to compute nodes.

Here, we give the essential information you need to know to start
computing on Midway 2 and Midway 3. For more detailed information on running
specialized compute jobs, see [Running jobs on midway](../running-jobs/index.md#running-jobs).

## Login nodes vs. compute nodes

Once you have connected to Midway 2 or 3 (see Connecting to RCC Resources (link)) you may work on one of the login nodes. Login nodes may be used for compiling and debugging code, installing software, editing and managing files, submitting jobs, or any other work that is not long-running or computationally intensive (see Using Midway (link)). *Login nodes should not be used for computionally intensive work.*

All intensive computations should be performed on compute nodes. Access to compute nodes can be obtained by submitting a job through the Slurm scheduler, or by requesting an interactive session. If you are unsure whether your computations will be intensive, please request an interactive session and continue your work once you have connected to the compute node.

**NOTE**: Running computationally intensive jobs on the login nodes prevents other users from efficiently using the cluster. RCC System Administrators may terminate your processes without warning if your processes disrupt other users’ work on the RCC cluster.

For more information on how to interact with Midway through the Slurm resource manager, see Using Midway (link)).

## Job Limits
To distribute computational resources fairly the RCC sets limits on the amount of computing resources that may be requested by a single user at any given time.

The maximum run-time for an individual job is **36 hours**. This applies to all batch and interactive jobs submitted to nodes in the general-access partitions. Groups participating in the cluster parternership program may customize resources limits for their partitions.

Additional information on limits can be found by entering the command 
```
rcchelp qos
``` 
on any login or compute node on Midway 2 or Midway 3.

Observe that these limits are often different depending on the partition.

Usage limits may change, so ```rcchelp qos``` will always give you the most up-to-date information.

If your research requires a temporary exception to a particular limit, you may apply for a special allocation. Special allocations are evaluated on an individual basis and may or may not be granted.