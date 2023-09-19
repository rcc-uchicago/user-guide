




## The RCC Workflow
This flowchart illustrates the workflow of a typical researcher using our HPC resources. 
<p align="center">
<img src="img/rcc_workflow.png" width="650" />
</p>  

## Overview of RCC's HPC Systems
The following tables provide a high-level summary of the various high-performance computing (HPC) systems that the RCC houses.  

**General Access Systems** (Accessible to any researcher with an RCC user account)

| System                                            | Description                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------|
| **[Midway3](midway23/midway_getting_started.md)** | The RCC's flagship HPC cluster for multi-purpose scientific computing |
| **[Midway2](midway23/midway_getting_started.md)** | HPC cluster for multi-purpose scientific computing                    |
| **[Skyway](skyway/skyway_overview.md)**           | Run Midway jobs on cloud computing platforms                          |
| **[DaLI](https://dali.uchicago.edu/using-dali/)** | Data Lifecycle Instrument, a data storage and software platform       |

**Restricted Access Systems** (Special permissions required for access)  

| System                                                               | Description                                          |
|----------------------------------------------------------------------|------------------------------------------------------|
| **[MidwayR3](https://sde-midwayr.rcc.uchicago.edu/user-guide/)**      | RCC's HPC cluster for sensitive data, housed within the [Secure Data Enclave](https://securedata.uchicago.edu/){:target="_blank"}  |  
| **[Beagle3](beagle3/beagle3_overview.md)**                           | A GPU-focused HPC cluster for life sciences research |
| **[MidwaySSD](https://midwayssd.rcc.uchicago.edu/using-midwayssd/)** | HPC cluster dedicated to social sciences research    |
| **[GM4](https://gm4.rcc.uchicago.edu/)**                             | A GPU HPC cluster for fast and efficient molecular simulations |

## Where to start?

* Researchers interested in using the RCC systems can [request an account](https://rcc.uchicago.edu/accounts-allocations/request-account){:target="_blank"}.  
* For Service Units (computing time) and storage resources, [request an allocation](https://rcc.uchicago.edu/accounts-allocations/request-allocation){:target="_blank"}.  
* If you would like to chat with an RCC specialist about what services are best for you, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support).

!!! tip "Know what you're looking for?"
    Check out the search bar in the top right of the page (e.g., search: "GPU")--it's surpisingly useful!

## Improve this user guide

If you come across any content that you think should be **changed or improved** (typo, out-of-date info, etc.), please feel free to do any of the following to help make the guide better:  

* [Contact us](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"}   
* Create an [Issue](https://github.com/rcc-uchicago/user-guide/issues/new){:target="_blank"} on GitHub

## Help Requests

You can [contact us](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"} to get technical user support for RCC systems related issues. Please provide the RCC staff with all useful information when requesting assistance and submit requests using your UChicago email address. In the following section, we include instructions to submit an informative ticket.  

* Write an informative subject/title to the ticket/email that can include details such as cluster name, software name, brief description of the issue
* Submit screenshots of the error message when possible
* Explain briefly what you are trying to do and the problem you are encountering
* Include instructions on how to reproduce your issue with relevant details such as:
    * Submit the list of modules that were loaded
        * Output of ``module list`` command
    * Submit the ``sbatch`` script, along with the ``.err`` and ``.out`` files
    * Submit the commands that led to the error, along with the error message
    * Submit the job ID for SLURM job related issues  
    * Submit the output of command ``pwd`` to inform us of your working directory  

We look forwarding to assisting you!