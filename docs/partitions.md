## Partitions
Midway compute nodes are organized into "partitions", subsets of nodes typically grouped by their hardware or ownership. When submitting a job via Slurm, you specify the partition it will run on by setting the `--partition=<partition>` flag. The SLURM scheduler will allocate your job to any available compute node within the specified partition. If a user wants to submit a job to the particular compute node, this can be requested by adding `--nodelist=<compute_node_ID>`. Most users will submit jobs to a 'shared' partition: a partition accessible to all Midway users. 
See the [Partitions page](midway_partitions.md) for information about all of the Midway partitions.

# Slurm Partitions

Partitions are collections of compute nodes with similar characteristics. Normally, a user submits a job to a partition (via Slurm flag `--partition=<partition>`) and then the job is allocated to any idle compute node within that partition. To get a full list of available partitions, type the following command in the terminal
```
sinfo -o "%20P %5D %14F %4c %8G %8z %26f %N"
```
The typical output will include: 

| Column           | Description                                                         |
|------------------|---------------------------------------------------------------------|
| `AVAIL_FEATURES` | Available features such as CPUs, GPUs, and internode interfaces         |
| `NODELIST`       | IDs of the compute nodes within the given partition                        |
| `NODES(A/I/O/T)` | Number of nodes by state in the format "allocated/idle/other/total" |
| `S:C:T`          | Number of sockets, cores, and threads                               |

If a user wants to submit their job to the particular compute node, this can be requested by adding the Slurm flag `--nodelist=<compute_node_ID>`. Compute nodes that differ in available features can be allocated by setting an additional constraint `--constraint=<compute_node_feature>`, for example `--constraint=v100` will allocate job to the compute node with NVIDIA V100 GPUs. 

You can also check the state of nodes in a given partition, for example caslake, by running the following command: 
```
nodestatus caslake
```

## Partitions
All Midway users can submit jobs to any of the shared partitions. 
Beagle3 users, in addition to shared partitions, have access to Beagle3 partitions too. 

**Parameters are shown per node**.
=== "Midway2 - Shared"

      |   <div style="width:73px">Partition</div>  | Nodes | <div style="width:20px">Cores</div> | CPU Type  | GPUs | GPU Type | Memory | <div style="width:158px">Nodelist</div> |
      |------------|-------|--------|-----------|------|----------|--------|----------|
      | `broadwl`    | 323   | 28   | e5-2680v4 | None | None     | 64 GB  | vary |
      | `broadwl-lc` | 14    | 28   | e5-2680v4 | None | None     | 64 GB  | midway2-[0203-0216] |
      | `broadwl-lc` | 1     | 28   | e5-2680v4 | None | None     | 128 GB | midway2-0439 |
      | `bigmem2`    | 5     | 28   | e5-2680v4 | None | None     | 512 GB | midway2-bigmem[01-04,06]|
      | `gpu2`       | 6     | 28   | e5-2680v4 | 4    | k80      | 128 GB | midway2-gpu[01-06] |

===+ "Midway3 - Shared"

      | Partition  | Nodes | Cores | CPU Type | GPUs    | GPU Type | Memory |<div style="width:140px">Nodelist</div>  |
      |------------|-------|-------|----------|---------|----------|--------|---------|
      | `caslake`   | 184   | 48   | gold-6248r | None  | None     | 192 GB       | vary |
      | `bigmem`    | 1     | 48   | gold-6248r | None  | None     | 768 GB       | midway3-0317|
      | `bigmem`    | 1     | 48   | gold-6248r | None  | None     | 1536 GB      | midway3-0318|
      | `amd-hm`    | 1     | 128  | epyc-7702  | None  | None     | 2048 GB      | midway3-0541|
      | `amd`       | 40    | 128  | epyc-7702  | None  | None     | 256 GB       | midway3-0[501-539,549]
      | `gpu`       | 1     | 48   | gold-6248r | 4     | a100     | 384 GB       | midway3-0294|
      | `gpu`       | 5     | 48   | gold-6248r | 4     | v100     | 192 GB       | midway3-[0277-0281] |
      | `gpu`       | 5     | 48   | gold-6248r | 4     | rtx6000  | 192 GB       | midway3-[0282-0286] |

=== "Beagle3 - Dedicated"

      | Partition | Nodes  | Cores | CPU Type  | GPUs | GPU Type|  Memory| Nodelist |
      | --------- | -------| ------| --------- | ---- | ------- | ------ | ---------|
      | `beagle3`   |   22   |  32  | gold-6346 | 4    |  a40    |    256 GB   | beagle3-[0001-0022] |
      | `beagle3`   |   22   |  32  | gold-6346 | 4    |  a100   |    256 GB   | beagle3-[0023-0044] |
      | `beagle3`   |   4    |  32  | gold-6346 | None |  None   |    512 GB   | beagle3-bigmem[1-4] |


=== "MidwaySSD - Dedicated"
      | Partition | Nodes | Cores/Node | CPU Type   | GPUs | GPU Type | Total Memory |
      |-----------|-------|------------|------------|------|----------|--------------|
      | `ssd`       | 18    | 48   | gold-6248r | None | None     | 192 GB       |
      | `ssd-gpu`   | 1     | 32   | gold-6346  | 4    | a100     | 256 GB       |


=== "KICP - Dedicated"
      | Partition | Nodes | Cores/Node | CPU Type   | GPUs | GPU Type | Total Memory |
      |-----------|-------|------------|------------|------|----------|--------------|
      | `kicp`      | 6     | 48   | gold-6248r | None | None     | 192 GB       |
      | `kicp-gpu`  | 1     | 32   | gold-5218  | 4    | v100     | 192 GB       |

### Partition QoS

This table details the job limits of each partition, set via a Quality of Service (QoS) accessible via 
```
rcchelp qos
```


=== "Midway2 QoS - Shared"

    | Partition | Max Nodes Per User | Max CPUs Per User | Max Jobs Per User | Max Wall Time |
    |-----------|--------------------|-------------------|-------------------|---------------|
    | `broadwl` | 100                | 2800              | 100               | 36 H          |
    | `gpu2`    | None               | None              | 10                | 36 H          |
    | `bigmem2` | None               | 112               | 5                 | 36 H          |


===+ "Midway3 QoS - Shared"

    | Partition | Max Nodes Per User | Max CPUs Per User | Max Jobs Per User | Max Wall Time |
    |-----------|--------------------|-------------------|-------------------|---------------|
    | `caslake` | 100                | 4800              | 1000              | 36 H          |
    | `gpu`     | None               | None              | 12                | 36 H          |
    | `bigmem`  | 96                 | 192               | 10                | 36 H          |
    | `amd`     | 64                 | 128               | 200               | 36 H          |


=== "MidwaySSD QoS - Dedicated"

    | Partition | AllowAccount | QoS     | Max Wall Time |
    |-----------|--------------|---------|---------------|
    | `ssd`       | ssd          | ssd     | 36 H          |
    | `ssd`       | ssd-stu      | ssd-stu | 36 H          |
    | `ssd-gpu`   | ssd          | ssd     | 36 H          |
    | `ssd-gpu`   | ssd-stu      | ssd-stu | 36 H          |

=== "KICP QoS - Dedicated"

    | Partition | AllowAccount | QoS     | Max Wall Time |
    |-----------|--------------|---------|---------------|
    | `kicp`      | kicp         | kicp    | 48 H          |
    | `kicp-gpu`  | kicp         | kicp    | 48 H          |

You may apply for a special allocation if your research requires a temporary exception to a particular limit. Special allocations are evaluated on an individual basis and may or may not be granted.

### Private Partitions (CPP)
These partitions are typically associated with a PI or group of PIs. They can be shared with other PIs or researchers across the University of Chicago and with external collaborators with a Midway account. 

* General Users: Check with your PI for more information. 
* PIs: Private partitions can be purchased via [Cluster Partnership Program](https://rcc.uchicago.edu/support-and-services/cluster-partnership-program){:target="_blank"} to accommodate the needs of your research group. QOS can be tuned at any time by submitting a request.

!!! note
    QoS for private and institutional partitions can be changed upon the owner's request. 

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

