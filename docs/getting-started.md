# Getting Started
<!-- From these links:
https://rcc.uchicago.edu/accounts-allocations -->

## What is RCC?
The University of Chicago Research Computing Center (RCC) is the home of multiple professionally managed high-performance computing clusters. In particular, Midway2, Midway3, Midway3-AMD, DaLI, Beagle3, MidwaySSD, and Skyway constitute the core of the RCC’s advanced computational infrastructure. 
Midway2 was introduced in 2016 as the successor to the RCC's first HPC cluster, Midway. Four years later, in 2021, the Midway3 cluster was brought online. 

Remember, DaLI, Midway2, and Skyway share a lot of options. Midway3, Midway3-AMD, and Beagle3 also are closely interconnected. In this user guide, we distinguish between these clusters whenever there are system-specific differences. 

!!! note
    We recommend Midway3 for new users, as it provides the latest hardware and software modules. 

## RCC accounts
The RCC offers two types of user accounts: 

* [Principal investigator (PI) accounts](https://rcc.uchicago.edu/accounts-allocations/pi-account-request)
* [General user accounts](https://rcc.uchicago.edu/accounts-allocations/general-user-account-request): A PI with an active RCC account must sponsor general users. 

More information about creating an account can be found on the [accounts and allocations page](https://rcc.uchicago.edu/accounts-allocations).

## Connecting 
After creating your RCC user account, you can [connect to an RCC login node](connecting.md). Depending on your operating system and desired user experience, there are several ways to connect to RCC's cluster **login nodes**. Login nodes are the "foyer" of the RCC's supercomputers. They are connected to the internet and enable you to transfer data to and from the system. 

## Transfering data
Once you successfully connect to login nodes, you can move your research data ([data transfer](data-transfer.md)) to your personal `/home/<cnetid>` and `scratch` directories. Also, you have access to your group's shared `project` directory ([data storage](data-storage.md)). 

## Running jobs
After transferring your research data, you can perform high-performance computation by running jobs (which call your scripts and programs) on **compute nodes** ([running jobs](jobs-overview.md)).

## Troubleshooting
Solutions to most issues can be found at our [FAQ pages](../FAQ/accounts-and-allocations.md).

If you need further assistance, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"}.
