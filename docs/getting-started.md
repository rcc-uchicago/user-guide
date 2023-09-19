![RCC Logo](img/rcc_logo.png)
# Getting Started
Welcome! This user guide provides information on accessing and using the University of Chicago [Research Computing Center's](https://rcc.uchicago.edu/) High-Performance Computing (HPC) resources. 

## What is RCC?
The University of Chicago Research Computing Center (RCC) is the home of multiple professionally managed high-performance computing clusters. In particular, Midway2, Midway3, Midway3-AMD, MidwaySSD, DaLI, Beagle3, GM4, and Skyway constitute the core of the RCC’s advanced computational infrastructure. 

Remember, DaLI and Midway2 share a lot of resources. Midway3, Midway3-AMD, and Beagle3 also are closely interconnected. In this user guide, we distinguish between these clusters whenever there are system-specific differences. 

### Midway2, Midway3, and Midway3-AMD
Midway2 was introduced in 2016 as the successor to the RCC's first HPC cluster, Midway. Four years later, in 2021, the Midway3 and Midway3-AMD clusters were brought online. 

!!! note
    We recommend Midway3 for new users, as it provides the latest hardware and software modules.

### [Beagle3](https://beag3.rcc.uchicago.edu/)
Beagle3 is a high-performance computing cluster funded by the NIH grant led by Professor Benoit Roux, the Amgen Professor of Biochemistry and Molecular Biology. The [project](https://biologicalsciences.uchicago.edu/news/features/beagle-3-gpu-cluster) benefits biomedical research with cutting-edge HPC resources for modeling and large-scale simulations of the molecular building blocks for biological functions. The cluster also serves research projects that employ recent advances in imaging technology, like cryo-electronic microscopy, for producing images of molecules at unprecedented resolution. The enormous amount of data rapidly generated needs commensurate amounts of computing horsepower to analyze. Beagle3 has been in service since February 2022. Beagle3 was preceded by the highly successful Beagle1 and Beagle2 supercomputer clusters and comprises 44 compute nodes, each with a 32-core Intel Xeon Gold 6346 CPU and 4 NVIDIA A100 graphics processing units (GPUs). 

### [DaLI](https://dali.uchicago.edu/using-dali/)
The Data Lifecycle Instrument (DaLI) enables the management and sharing of data from instruments and observations, allowing researchers to:

* Acquire, transfer, process, and store data from experiments and observations in a unified workflow.
* Manage data collections over their entire lifecycle.
* Share and publish data.
* Enhance outreach and education opportunities.

### [MidwaySSD](https://midwayssd.rcc.uchicago.edu/using-midwayssd/)
MidwaySSD is a high-performance computing cluster within the Midway3 ecosystem dedicated to computationally intensive Social Science Division research and educational excellence. 

### [GM4](https://gm4.rcc.uchicago.edu/)
The GPU-enabled Multiscale Materials Modeling and Machine-learning (GM4) cluster is a high-performance GPU cluster tailored for fast and efficient simulations, including molecular dynamics (MD), hybrid particle-continuum, mesoscale, and continuum simulations. This state-of-the-art research instrument was awarded to the University of Chicago researchers by the National Science Foundation (NSF)  under the Major Research Instrumentation (MRI) program. GM4 provides a unique computational resource that enables new collaborative efforts in algorithm and software development at the interface between molecular engineering, physics, chemistry, biology, computer science, and materials science. 

### [Skyway](https://cloud-skyway.rcc.uchicago.edu/)
Skyway is an integrated platform developed at the RCC to allow users to burst computing workloads from the on-premise RCC cluster, Midway, to run on remote commercial cloud platforms such as Amazon AWS, Google GCP, and Microsoft Azure. Skyway enables users to run computing tasks in the cloud from Midway seamlessly without needing to learn how to provision cloud resources. Since the user does not need to set up or manage cloud resources, the result is improved productivity with a minimum learning curve. Skyway uses SLURM as a resource manager in the cloud. Resources in the cloud have the same configuration, software modules, and file storage systems as Midway2. 

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
