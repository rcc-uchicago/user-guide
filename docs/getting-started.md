# Getting Started on Midway
<!-- From these links:
https://rcc.uchicago.edu/accounts-allocations -->

## What is Midway?
Midway2 and Midway3 are professionally-managed high-performance computing clusters that constitute the core of the RCC’s advanced computational infrastructure. Midway2 was introduced in 2016 as the successor to the RCC's first HPC cluster, Midway. Four years later, in 2021, the Midway3 cluster was brought online. In this guide, we use "Midway" to refer to both existing clusters, as much of the user experience for Midway2 and Midway3 is similar. We distinguish between the two whenever there are system-specific differences.  

!!! note
    We recommend Midway3 for new users, as it provides the latest hardware and software modules.

## Gaining Access
The RCC offers two types of user accounts: a PI Account and a General User Account. All General Users must be sponsored by a PI with an active RCC account. More information about creating an account can be found on the [Accounts and Allocations page](https://rcc.uchicago.edu/accounts-allocations){:target="_blank"}.

## Connecting and Running Jobs
After your RCC User account is created, you will connect to a Midway login node ([Connecting to Midway](connecting.md)). There are several different ways to connect, depending on your operating system and desired user experience. Login nodes are the "foyer" of the Midway supercomputer. They are connected to the internet and enable you to transfer data to and from the system. 

Once you successfully connect to Midway, you'll move data ([Data Transfer](data-transfer.md)) to your personal `home` directory, and/or your personal `scratch` directory, and/or your group's shared `project` directory ([Data Storage](data-storage.md)). Then, you will be able to perform high-performance computation by running jobs (which call your scripts and programs) on compute nodes ([Running Jobs](jobs-overview.md)).

## Troubleshooting

Solutions to most issues can be found at our [FAQ pages](../FAQ/accounts-and-allocations.md).

If you need further assistance, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"}.
