# Slurm Partitions

Partitions are collections of compute nodes with similar characteristics. To get a full list of available partitions, type the following command in the terminal
```
sinfo -o "%20P %5D %14F %4c %8G %8z %26f %N"
```
The (S:C:T) column refers to the number of sockets, cores, and threads. The NODES(A/I/O/T) column lists the number of nodes by state in the format "allocated/idle/other/total".

## Shared Partitions
All Midway users can submit jobs to any of the following shared partitions:
<!-- THIS COMMNAD WORKS ON MIDWAY2 BUT NOT ON MIDWAY3 - SHOULD BE FIXED
The list of shared partitions can be invoked by -->
<!-- ```
rcchelp sinfo shared
``` -->
=== "Midway2"
      | Partition | Nodes  | CPUs/node |   Cores/node   | CPU Type  | GPUs/node | GPU Type| Total Memory|
      | --------- | ------ | ----------| -------------- | ----------| --------- | ------- | ----------- |
      | broadwl   |   8    |     2     |       40       | gold-6148 | 4         |  v100   |    192 GB   |
      | broadwl   |   2    |     2     |       40       | gold-6148 | None      |  None   |    192 GB   |
      | broadwl   |   187  |     2     |       28       | e5-2680v4 | None      |  None   |    64 GB    |
      | broadwl   |   164  |     2     |       28       | e5-2680v4 | None      |  None   |    64 GB    |
      | broadwl   |   3    |     2     |       28       | e5-2680v4 | None      |  None   |    64 GB    |
      | broadwl-lc|   14   |     2     |       28       | e5-2680v4 | None      |  None   |    64 GB    | 
      | bigmem2   |   5    |     2     |       28       | e5-2680v4 | None      |  None   |    512 GB   |
      | gpu2      |   6    |     2     |       28       | e5-2680v4 | 2         |  k80    |    128 GB   |
      | gpu2      |   1    |     2     |       40       | gold-6148 | 4         |  v100   |    96 GB    |

===+ "Midway3"
      | Partition | Nodes  | CPUs/node |   Cores/node   | CPU Type  | GPUs/node | GPU Type| Total Memory|
      | --------- | ------ | ----------| -------------- | ----------| --------- | ------- | ----------- |
      | caslake   |   203  |     2     |  48            | gold-6248r| None      |  None   |    192 GB   | 
      | bigmem    |   1    |     2     |  48            | gold-6248r| None      |  None   |    768 GB   |
      | bigmem    |   1    |     2     |  48            | gold-6248r| None      |  None   |    1536 GB  |
      | amd-hm    |   1    |     2     |  128           | epyc-7702 | None      |  None   |    2048 GB  |
      | amd       |   1    |     2     |  128           | epyc-7702 | None      |  None   |    1024 GB  |
      | amd       |   40   |     2     | 128            | epyc-7702 | None      |  None   |    256 GB   |
      | gpu       |   5    |     2     |  48            | gold-6248r| 4         |  v100   |    192 GB   |
      | gpu       |   5    |     2     |  48            | gold-6248r| 4         |  rtx6000|    192 GB   |

## Shared Partition QOS

This table details the job limits of each partition, set via a Quality of Service (QOS) accessible via `rcchelp qos`.

=== "Midway2 QOS"

    | Partition | Max Nodes Per User| Max CPUs Per User  | Max Jobs Per User| Max Wall Time | 
    | --------- | ----------------- | ------------------ | ---------------- | ------------- |
    | `broadwl` | 100               |            2800    |             1000 |  36 H         |
    | `gpu2`    | None              |            None    |             10   |  36 H         |
    | `bigmem2` | None              |            112     |             5    |  36 H         |


===+ "Midway3 QOS"

    | Partition | Max Nodes Per User| Max CPUs Per User  | Max Jobs Per User| Max Wall Time | 
    | --------- | ----------------- | ------------------ | ---------------- | ------------- |
    | `caslake` | 100               |            4800    |             1000 |  36 H         |
    | `gpu`     | None              |            None    |             500  |  36 H         |
    | `bigmem`  | 96                |            192     |             10   |  36 H         |
    | `amd`     | 64                |            128     |             200  |  36 H         |

If your research requires a temporary exception to a particular limit, you may apply for a special allocation. Special allocations are evaluated on an individual basis and may or may not be granted.



## Institutional Partitions
Faculty and their group members can take advantage of institutional partitions dedicated to research withing UChicago divisions, departments, and institutions:

* ssd, ssd-gpu:   Social Science Research       
> SSD Faculty (By default) and their group members ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"}) 
* kicp, kicp-gpu: Cosmological Physics Research 
> KICP Faculty (By default) and their group members ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"})
* beagle3:        Biomedical Research           
> UChicago Faculty and their group members (Once PI is approved) 
* qnext:          Quantum Information Science   
> Q-Next Faculty and their group members
*

<!-- === "Midway2 NEED TO CHECK WITH KATHY"
      | Partition | Nodes  | CPUs |
      | --------- | -------| -----|
      | broadwl   |   8    |  40  |
      | broadwl   |   2    |  40  |
      | broadwl   |   187  |  28  |
      | broadwl   |   164  |  28  |
      | broadwl   |   3    |  28  |
      | broadwl-lc|   14   |  28  |
      | bigmem2   |   5    |  28  |
      | gpu2      |   6    |  28  |
      | gpu2      |   1    |  40  | -->

===+ "Midway3"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- |
      | ssd       |   18   |  48  | gold-6248r| None |  None   |    192 GB   |  36:00:00  |
      | ssd-gpu   |   1    |  32  | gold-6346 | 4    |  a100   |    256 GB   |  36:00:00  |
      | kicp      |   6    |  48  | gold-6248r| None |  None   |    192 GB   |  48:00:00  |
      | kicp-gpu  |   1    |  32  | gold-5218 | 4    |  v100   |    192 GB   |  48:00:00  |
      | qnext     |   40   |  128 | epyc-7702 | None |  None   |    256 GB   |  36:00:00  |


## Private Partitions
These partitions are typically associated with a research group with access approved by PI. They can be shared with other PIs or researchers across the University of Chicago and also with external collaborators who have midway accounts ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"}). Private partitions can be purchased via [RCC Cluster Partnership Program](https://rcc.uchicago.edu/support-and-services/cluster-partnership-program){:target="_blank"} to better accomodate the needs of a research group.

## Do I Have Access to a Partition?
To check if you have access to a partition, first determine which groups your account belongs to: 
```
groups
```
and then check AllowAccounts field in the partion summary: 
```
scontrol show partition <partition_name>
```
If AllowAccount is set to All then it is a shared partition available to all users. Otherwise, it is an institutional or private partition and one of your groups must match the AllowAccounts field in order to submit SLURM jobs to that partition. 

<!-- === "MidwayR"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit | Local Scratch | Nodelist     |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- | ------------- | ------------ |
      | skylake   |   4    |  40  | gold-6148 | None |  None   |    96 GB    |  36h or 7d |   900 MB      | sde[001-004] |
      | caslake-bigmem| 1  |  40  | gold-6248 | None |  None   |    1536 GB  |  36h or 7d |   900 MB      | sde005       |
      | booth     |   1    |  48  | gold-6248 | None |  None   |    1536 GB  | 7-00:00:00 |  1.8 GB       | sde006       | 
      | booth     |   2    |  48  | gold-6248r| None |  None   |    384 GB   | 7-00:00:00 |  1.8 GB       | sde[007-008] |
      | booth     |   1    |  48  | gold-6248r| 2    |  v100   |    384 GB   | 7-00:00:00 |  1.8 GB       | sde009       | -->
<!-- ```
sacctmgr list qos format=Name,MaxWall,MaxSubmitPU
``` -->
