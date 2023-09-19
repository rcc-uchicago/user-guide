# Getting Started
<!-- From these links:
https://rcc.uchicago.edu/accounts-allocations -->

## What is RCC?
The University of Chicago Research Computing Center (RCC) is the home of multiple professionally managed high-performance computing clusters. In particular, Midway2, Midway3, Midway3-AMD, DaLI, Beagle3, MidwaySSD, and Skyway constitute the core of the RCC’s advanced computational infrastructure. 

Remember, DaLI, Midway2, and Skyway share a lot of options. Midway3, Midway3-AMD, and Beagle3 also are closely interconnected. In this user guide, we distinguish between these clusters whenever there are system-specific differences. 

### Midway2 and Midway3
Midway2 was introduced in 2016 as the successor to the RCC's first HPC cluster, Midway. Four years later, in 2021, the Midway3 cluster was brought online. 

!!! note
    We recommend Midway3 for new users, as it provides the latest hardware and software modules.

### Beagle2
Beagle3 is a high-performance computing cluster funded by the NIH grant led by Professor Benoit Roux, the Amgen Professor of Biochemistry and Molecular Biology. The [project](https://biologicalsciences.uchicago.edu/news/features/beagle-3-gpu-cluster) benefits biomedical research with cutting-edge HPC resources for modeling and large-scale simulations of the molecular building blocks for biological functions. The cluster also serves research projects that employ recent advances in imaging technology, like cryo-electronic microscopy, for producing images of molecules at unprecedented resolution. The enormous amount of data rapidly generated needs commensurate amounts of computing horsepower to analyze. Beagle3 has been in service since February 2022.

Beagle3 comprises 44 compute nodes, each with a 32-core Intel Xeon Gold 6346 CPU and 4 NVIDIA A100 graphics processing units (GPUs). 


## RCC accounts
The RCC offers two types of user accounts: 

* [Principal investigator (PI) accounts](https://rcc.uchicago.edu/accounts-allocations/pi-account-request)
* [General user accounts](https://rcc.uchicago.edu/accounts-allocations/general-user-account-request): A PI with an active RCC account must sponsor general users. 

More information about creating an account can be found on the [accounts and allocations page](https://rcc.uchicago.edu/accounts-allocations).

## Connecting 
After creating your RCC user account, you can [connect to an RCC login node](connecting.md). Depending on your operating system and desired user experience, there are several ways to connect to RCC's cluster **login nodes**. Login nodes are the "foyer" of the RCC's supercomputers. They are connected to the internet and enable you to transfer data to and from the system. 

## Transfering data
Once you successfully connect to login nodes, you can move your research data ([data transfer](data-transfer.md)) to your personal directories. Also, you have access to your group's shared directory ([data storage](data-storage.md)). 

## Running jobs
After transferring your research data, you can perform high-performance computation by running jobs (which call your scripts and programs) on **compute nodes** ([running jobs](jobs-overview.md)).

## Troubleshooting
Solutions to most issues can be found at our [FAQ pages](../FAQ/accounts-and-allocations.md).

If you need further assistance, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support).
