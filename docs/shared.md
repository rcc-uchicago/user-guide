# SHARED
<!-- From these links:
https://www.lib.uchicago.edu/about/news/uchicago-launches-shared-a-new-data-platform-for-research-collaboration-and-discovery/ -->

## What is SHARED?

The University of Chicago has received funding from the National Science Foundation (NSF) under Award No 2346746, to develop SHARED, the Secure Hub for Access, Reliability, and Exchange of Data. This new storage platform will advance research through robust capabilities for data storage, accessibility, sharing and integration with national and global data federations. It will provide critical storage capacity for research and supporting data science curricula development and education. For more information please see [this reference](https://dl.acm.org/doi/10.1145/3708035.3736042).

Designed as a cornerstone of UChicago's data lifecycle strategy, from collection and analysis to publication and archiving, SHARED will integrate with the University’s institutional repository, Knowledge@UChicago, and connect to national research networks like the Open Science Grid (OSG). The SHARED project and platform is led by the University of Chicago Library and Research Computing Center (RCC), with contributions from University IT Services, Data Science Institute, and Physical Sciences Division. The SHARED platform will be essential for enabling partner faculty to meet federal requirements for data management and sharing.

## Allocations

The majority of the storage available in SHARED is reserved and for the projects and research groups that are part of the grant. Each project has a directory under `/shared` and the group ownership of these directories are initially assigned to the main PIs of each project. Requests for changes of ownership, creation of new groups, or questions about permissions can be submitted to [shared@rcc.uchicago.edu](mailto:shared@rcc.uchicago.edu). 

There are reservations of 50 TB will be reserved for educational, broader impact, and outreach activities, including open pedagogical data sets. In addition, an initial 50 TB will be reserved for open access data repositories for published research findings and the data that can be used to verify the published findings in accordance with FAIR principles. Allocation policies will be reviewed periodically by the SHARED executive committee.

## Access

There are different services and gateways for the members of the grant PIs to access the SHARED storage system, as listed below:

* Mount point in the Midway3 login nodes `/shared`
* Mount point in the Midway2 and DaLI login nodes `/shared`
* [Globus](globus/share-files.md) collection `UChicago RCC SHARED`
* [SAMBA](samba.md) share: connecting to the following server using the username `ADLOCAL\[cnetid]`
     * Windows: `\\shared-smb.rcc.uchicago.edu\shared` 
     * MacOS: `smb://shared-smb.rcc.uchicago.edu/shared`

Project members can submit requests for additional gateway services and storage endpoints to the email [shared@rcc.uchicago.edu](mailto:shared@rcc.uchicago.edu). A member of the SHARED team will analyze the feasibility and contact the requestor for additional details.

Please note:

* The `/shared` mount points in the Midway systems is available only in the login nodes and cannot be mounted in the compute nodes as the SHARED filesystem is built for resiliency, data durability and stability, and not optimized for highly parallel I/O workloads.
* For security reasons the SAMBA share can only be accessed from the UChicago networks, i.e., campus network or cVPN.

Data can be transferred between `/shared` and other [storage spaces](storage/main.md) in the Midway ecosystem using command line interface tools such as `cp`, `scp`, `rsync` and `rclone`.

### Backup

There are daily and weekly snapshots of `/shared` taken automatically daily and weekly under the
directory `/shared/.snap`. Each snapshot is timestamped and named such as:

```
scheduled-2026-04-20-20_00_00_UTC
```

Users can find their data under the corresponding PI folders within each snapshot.

The retention policy is to keep the last 7 daily snapshots, and the last 4 weekly snapshots.

## Troubleshooting

For further assistance, please send an email to [shared@rcc.uchicago.edu](mailto:shared@rcc.uchicago.edu) and [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"}
