# Slurm Partitions

Partitions are collections of compute nodes with similar characteristics. To get a full list of available partitions, type the following command in the terminal
```
sinfo -o "%20P %5D %14F %4c %8G %8z %26f %N"
```
The output of this command is self-explanatory. The (S:C:T) column refers to the number of sockets, cores, and threads. The NODES(A/I/O/T) column lists the number of nodes by state in the format "allocated/idle/other/total".

## Shared Partitions
All Midway users can submit jobs to shared partitions. 
<!-- THIS COMMNAD WORKS ON MIDWAY2 BUT NOT ON MIDWAY3 - SHOULD BE FIXED
The list of shared partitions can be invoked by -->
<!-- ```
rcchelp sinfo shared
``` -->

=== "Midway2"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit | MaxCPUsPerUser |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- | -------------- |
      | broadwl   |   8    |  40  | gold-6148 | 4    |  v100   |    192 GB   |  36:00:00  |       2800     |
      | broadwl   |   2    |  40  | gold-6148 | None |  None   |    192 GB   |  36:00:00  |       2800     |
      | broadwl   |   187  |  28  | e5-2680v4 | None |  None   |    64 GB    |  36:00:00  |       2800     | 
      | broadwl   |   164  |  28  | e5-2680v4 | None |  None   |    64 GB    |  36:00:00  |       2800     |
      | broadwl   |   3    |  28  | e5-2680v4 | None |  None   |    64 GB    |  36:00:00  |       2800     |
      | broadwl-lc|   14   |  28  | e5-2680v4 | None |  None   |    64 GB    |  36:00:00  |       -        | 
      | bigmem2   |   5    |  28  | e5-2680v4 | None |  None   |    512 GB   |  36:00:00  |       112      |
      | gpu2      |   6    |  28  | e5-2680v4 | 2    |  k80    |    128 GB   |  36:00:00  |       -        | 
      | gpu2      |   1    |  40  | gold-6148 | 4    |  v100   |    96 GB    |  36:00:00  |       -        |

===+ "Midway3"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit | MaxCPUsPerUser |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- | -------------- |
      | caslake   |   203  |  48  | gold-6248r| None |  None   |    192 GB   |  36:00:00  |       4800     |
      | bigmem    |   1    |  48  | gold-6248r| None |  None   |    768 GB   |  36:00:00  |       96       |
      | bigmem    |   1    |  48  | gold-6248r| None |  None   |    1536 GB  |  36:00:00  |       96       |
      | amd-hm    |   1    |  128 | epyc-7702 | None |  None   |    2048 GB  |  36:00:00  |       128      |
      | amd       |   1    |  128 | epyc-7702 | None |  None   |    1024 GB  |  36:00:00  |       None     |
      | amd       |   40   |  128 | epyc-7702 | None |  None   |    256 GB   |  36:00:00  |       None     |
      |schmidt-gpu|   1    |  48  | gold-6248r| 4    |  a100   |    384 GB   |  36:00:00  |       None     |
      | gpu       |   5    |  48  | gold-6248r| 4    |  v100   |    192 GB   |  36:00:00  |       96       |
      | gpu       |   5    |  48  | gold-6248r| 4    |  rtx6000|    192 GB   |  36:00:00  |       96       |


## Institutional Partitions
Faculty and their group members can take advantage of institutional partitions dedicated to research withing UChicago divisions, departments, and institutions:

* ssd, ssd-gpu:   Social Science Research       
> SSD Faculty (By default) and their group members ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"}) 
* kicp, kicp-gpu: Cosmological Physics Research 
> KICP Faculty (By default) and their group members ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"})
* beagle3:        Biomedical Research           
> UChicago and UCMC Faculty (??Apply??) and their group members (Once PI is approved) 
* qnext:          Quantum Information Science   
> Q-Next Faculty ([Apply](https://rcc.uchicago.edu/accounts-allocations/join-different-pi-account){:target="_blank"}) and their group member (Once PI is approved) 
* sjfkfloor2:     ??? Visualization Laboratory   >> ???
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
      | beagle3   |   22   |  32  | gold-6346 | 4    |  a40    |    256 GB   |  48:00:00  |
      | beagle3   |   22   |  32  | gold-6346 | 4    |  a100   |    256 GB   |  48:00:00  |
      | beagle3   |   4    |  32  | gold-6346 | None |  None   |    512 GB   |  48:00:00  |
      | qnext     |   40   |  128 | epyc-7702 | None |  None   |    256 GB   |  36:00:00  |
      | sjfkfloor2|   1    |  48  | gold-6248r| 4    |  a100   |    384 GB   |  36:00:00  |


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
If AllowAccount is set to All then it is a shared partition available to all users. Otherwise, it is an institutional or private partition and one of your groups must match the AllowAccounts field to have access to that partition. 

<!-- === "MidwayR"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit | Local Scratch | Nodelist     |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- | ------------- | ------------ |
      | skylake   |   4    |  40  | gold-6148 | None |  None   |    96 GB    |            |   900 MB      | sde[001-004] |
      | caslake-bigmem| 1  |  40  | gold-6248 | None |  None   |    1536 GB  |            |   900 MB      | sde005       |
      | booth     |   1    |  48  | gold-6248 | None |  None   |    1536 GB  |            |  1.8 GB       | sde006       | 
      | booth     |   2    |  48  | gold-6248r| None |  None   |    384 GB   |            |  1.8 GB       | sde[007-008] |
      | booth     |   1    |  48  | gold-6248r| 2    |  v100   |    384 GB   |            |  1.8 GB       | sde009       | -->