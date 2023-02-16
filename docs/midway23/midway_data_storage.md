# Data Storage

Midway2 and Midway3 have a high-performance GPFS shared file system that houses users' **home** directories,
shared **project** spaces, and high-throughput **scratch** space. The project and scratch directories of Midway2 and Midway3 are 'cross-mounted' and accessible from both systems' login and compute nodes, while `/home`, `/software`, and `/snapshots` are specific to each cluster and its respective login nodes.
<br/><br/>
![Midway Storage](img/data_management/midway23_storage.jpg)

## Quotas

The amount of data that can be stored in home directories, project directories, and shared scratch directories is controlled by quota. RCC enforces hard and soft limits on quotas. A soft quota can be exceeded for a short period of time called a grace period.  The hard quota cannot be exceeded under any circumstances.

=== "Midway2"
      | Name | <div style="width:200px">Location</div> | <div style="width:100px">Soft Quota</div> | <div style="width:100px">Hard Quota</div> | Suitable For  |
      |----------|-----------------------------|------------------------------|---------------------|---------------------------|
      | Home    | `/home/<CNetID>`            | 30 GB <br /> (or 300K files) | 35 GB <br /> (or 1M files) | Personal scripts & files  |
      | Project | `/project2/<PI CNetID>`     | variable                     | variable                   | Shared data, environments |
      | Scratch | `/scratch/midway2/<CNetID>` | 100 GB                       | 2 TB                       | Output of jobs            |

===+ "Midway3"
      | Name | <div style="width:200px">Location</div> | <div style="width:100px">Soft Quota</div> | <div style="width:100px">Hard Quota</div> | Suitable For  |
      |---------|-----------------------------|------------------------------|----------------------------|---------------------------|
      | Home    | `/home/<CNetID>`            | 30 GB <br /> (or 300K files) | 35 GB <br /> (or 1M files) | Personal scripts & files  |
      | Project | `/project/<PI CNetID>`      | variable                     | variable                   | Shared data, environments |
      | Scratch | `/scratch/midway3/<CNetID>` | 100 GB                       | 2 TB                       | Output of jobs            |

### Checking available storage

To check your current quotas use `rcchelp quota`. Typical output may look like this
```
---------------------------------------------------------------------------
fileset          type                   used      quota      limit    grace
---------------- ---------------- ---------- ---------- ---------- --------
home             blocks (user)         8.77G     30.00G     35.00G     none
                 files  (user)        157865     300000    1000000     none
scratch          blocks (user)        16.07G    100.00G      5.00T     none
                 files  (user)        193028   10000000   20000000     none
---------------- ---------------- ---------- ---------- ---------- --------
>>> Capacity Filesystem: project2 (GPFS)
---------------- ---------------- ---------- ---------- ---------- --------
rcc              blocks (group)      259.10T    500.00T    501.00T     none
                 files  (group)     45825436  384500000  385500000     none
---------------- ---------------- ---------- ---------- ---------- --------
---------------------------------------------------------------------------
```
The following table describes the fields:

| Field | Meaning |
| ----- | ------- |
| fileset| File set or file system where this quota is valid.|
| type| Type of quota. *Blocks* are the amount of consumed disk space. *Files* are the number of files in a directory. Blocks or files quotas can be set at the user or group level.|
| used| The amount of disk space consumed or the number of files in the specified location.|
| quota| The *soft quota* (disk space or file count) associated with the specified location. It is possible for usage to exceed the soft quota for the grace period or up to the hard limit.|
| limit| The *hard quota* (disk space or file count) associated with the specified location. When your usage exceeds this limit, you will NOT be able to write to that filesystem.|
| grace| The amount of time remaining that the soft quota can be exceeded. *None* means that the quota is not exceeded. After a soft quota has been exceeded for longer than the grace period, it will no longer be possible to create new files.|

!!! warning "Over quota?"
      Errors may occur if you are over quota. See our [FAQ page on data management](../FAQ/data_management_faq.md) for multiple strategies for getting back under quota.

## Purchasing More Storage  
Additional storage is available through the [Cluster Partnership Program](https://rcc.uchicago.edu/support-and-services/cluster-partnership-program){:target="_blank"},
a [Research I Allocation](https://rcc.uchicago.edu/research-allocation-request){:target="_blank"}, [Research II Allocation](https://rcc.uchicago.edu/research-allocation-request-II){:target="_blank"} or, in certain circumstances,
a [Special Allocation](https://rcc.uchicago.edu/special-allocation-request){:target="_blank"}.

## Persistent Space

Persistent spaces are where data go for medium- to long-term storage. The two persistent storage locations on Midway are the `home` and `project` directories. Both directories have frequent file system snapshots and tape backup for data protection.

### Home Directories

Every RCC user has a home directory located at `/home/<CNetID>`. The `HOME` environment variable points to this location. The home directory is accessible from all RCC compute systems and is generally used for storing frequently used items such as source code, binaries, and scripts. By default, a home directory is only accessible by its owner (mode `0700`) and is suitable for storing files which do not need to be shared with others.

### Project Directories

All RCC PI Groups are allocated a Project Directory located at `/project/<PI CNetID>` or
`/project2/<PI CNetID>` where *<PI CNetID>* is the CNetID of your RCC PI account holder. These directories
are accessible by all members of the PI Group and are generally used for storing
files which need to be shared by members of the group.  

The default permissions for files
and directories created in a project directory allow group read/write with the
group sticky bit set (mode `2770`). The group ownership is set to the PI group.

## Scratch Space

### Shared Scratch Space

High performance shared scratch space can be accessed using the SCRATCH environment variable. This scratch space is intended to be used for reading or writing data required by jobs running on the cluster. If a user is over quota, they can use scratch space as a temporary location to hold files (and/or compress them for archival purposes) **but as scratch space is neither snapshotted nor backed up, it should always be viewed as temporary.**

!!! warning
      It is the responsibility of the user to ensure any important data in scratch space is moved to persistent storage.  Scratch space is meant to be used for temporary, short-term  storage only.

The default permissions for scratch space allow access only by its owner (mode `0700`). The standard quota
for the high performance scratch directory is 5 TB with a 100GB soft limit.  The grace period that the soft limit may be
exceeded is 30 days for shared scratch space.

### Local Scratch Space
There is also a scratch space that resides on the local solid-state drives of each node and can only be used for jobs that does not require distributed parallel I/O. The capacity of the local SSD on Midway3 is 960 GB, but the actual amount of usable space will be less than this and may depend on the usage of other users utilizing the same node if your job resource request does not give you exclusive access to a node.<br></br>
<!-- There is presently no Slurm post script to clean up the local scratch, so please be mindful to clean up this space after any job. -->

It is recommended that users use the local scratch space if they have high throughput I/O of many small files ( size < 4 MB) for jobs that are not distributed across multiple nodes.To write files to local scratch use environment variables `$TMPDIR` or `$SLURM_TMPDIR`, which are set to `/tmp/jobs/${SLURM_JOB_ID}` and add a line at the very end of your Slurm script to copy or move the output to /project to save the output. Otherwise, all temporary files will be removed once the job is completed or crashed.

## Cost-Effective Data Storage  
In addition to high-performance GPFS file system, RCC also offers Cost-effective Data Storage (CDS) through the
[Cluster Partnership Program](https://rcc.uchicago.edu/support-and-services/cluster-partnership-program) for long-term data storage. CDS is only available from login nodes and is meant
to be used as a storage for less frequently accessed data. Before performing any computation on the data stored
on CDS, it first needs to be copied to the GPFS file system.  

## Data Recovery and Backups

### Snapshots

Automated snapshots of home and project directories are available in case
of accidental file deletion or other problems. Currently snapshots are
available for these time periods:

<!-- * 4 hourly snapshots -->
<!-- * 7 daily snapshots -->
<!-- * 4 weekly snapshots -->
| Directory            | Snapshot kept        | Snapshot Path                                        |
|----------------------|----------------------|------------------------------------------------------|
| `/home/<CNetID>`     | 7 daily and 2 weekly | `/snapshots/home/SNAPSHOT/home/<CNetID>`             |
| `/project/<folder>`  | 7 daily and 2 weekly | `/snapshots/project/SNAPSHOT/project/<any_folder>`   |
| `/project2/<folder>` | 7 daily and 4 weekly | `/snapshots/project2/SNAPSHOT/project2/<any_folder>` |

The snapshots for the `home` and `project` directories are available from the login nodes. The {SNAPSHOT} refers to the time of the backup, e.g. daily-YYYY-MM-DD.05h30 or weekly-YYYY-MM-DD.05h30. To view the available snapshots of the `home` directory, for example, use the command `ls /snapshots/home` to restore a file from a snapshot, simply copy the file to where you want it with either `cp` or `rsync`.
