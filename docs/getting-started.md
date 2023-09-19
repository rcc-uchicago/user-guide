# Getting Started
<!-- From these links:
https://rcc.uchicago.edu/accounts-allocations -->

## What is RCC?
The University of Chicago Research Computing Center (RCC) is the home of multiple professionally managed high-performance computing clusters. In particular, Midway2, Midway3, Midway3-AMD, DaLI, Beagle3, MidwaySSD, and Skyway constitute the core of the RCC’s advanced computational infrastructure. 
Midway2 was introduced in 2016 as the successor to the RCC's first HPC cluster, Midway. Four years later, in 2021, the Midway3 cluster was brought online. 

Remember, DaLI, Midway2, and Skyway share a lot of options. Midway3, Midway3-AMD, and Beagle3 also are closely interconnected. In this user guide, we distinguish between the clusters whenever there are system-specific differences. 

!!! note
    We recommend Midway3 for new users, as it provides the latest hardware and software modules. 

## RCC accounts
The RCC offers two types of user accounts: 

* [Principal investigator (PI) account](https://rcc.uchicago.edu/accounts-allocations/pi-account-request)
* [General user account](https://rcc.uchicago.edu/accounts-allocations/general-user-account-request): All general users must be sponsored by a PI with an active RCC account. 

More information about creating an account can be found on the [Accounts and Allocations page](https://rcc.uchicago.edu/accounts-allocations).

## Connecting and running jobs
After your RCC User account is created, you will connect to a Midway login node ([Connecting to Midway](connecting.md)). There are several different ways to connect, depending on your operating system and desired user experience. Login nodes are the "foyer" of the Midway supercomputer. They are connected to the internet and enable you to transfer data to and from the system. 

Once you successfully connect to Midway, you'll move data ([Data Transfer](data-transfer.md)) to your personal `home` directory, and/or your personal `scratch` directory, and/or your group's shared `project` directory ([Data Storage](data-storage.md)). Then, you will be able to perform high-performance computation by running jobs (which call your scripts and programs) on compute nodes ([Running Jobs](jobs-overview.md)).

## Troubleshooting

Solutions to most issues can be found at our [FAQ pages](../FAQ/accounts-and-allocations.md).

If you need further assistance, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"}.
