# Allocations and Service Units FAQ

## What is an allocation?
An allocation is a system designed to ensure fair usage of computing resources (service units) and storage (Gigabytes) granted to a Principal Investigator (PI) or an education account.

### Service Units (SUs)
In simple terms, you consume service units as you run jobs on shared compute nodes. Applying for service units incurs no cost for PIs and is solely a means to ensure fair usage of shared compute nodes. Please refer to [RCC Allocations](https://rcc.uchicago.edu/accounts-allocations/allocation-service-units) for more detailed information. Note that certain nodes or partitions, such as those in the Cluster Partnership Program, as well as private nodes and partitions like Beagle3 and MidwaySSD, do not consume service units when utilized since they are not shared resources. 

### Storage
RCC offers a limited volume of free group share storage alongside service units when a PI applies for an allocation. If you require additional storage space beyond what is allocated, please contact our CPP team at cpp@rcc.uchicago.edu.

## What is a service unit (SU)?
As you execute jobs on shared compute nodes at RCC, you deplete service units, akin to utilizing fuel. By imposing a cap on the number of service units that can be consumed per academic year, we ensure equitable utilization of our shared compute nodes. For a more precise definition, please visit [RCC Service Units](https://rcc.uchicago.edu/accounts-allocations/user-guidelines).

## How do I obtain an allocation?
For detailed information on obtaining an allocation, please refer to [RCC Allocations](https://rcc.uchicago.edu/accounts-allocations/allocation-service-units).

## How does RCC calculate the service units used for running a job on shared nodes?
For insights into how RCC calculates the service units expended during job execution on shared nodes, please consult [RCC Allocations](https://rcc.uchicago.edu/accounts-allocations/calculations-service-units).

## How do I check how many service units I have remaining on my allocation?
The `accounts` tool offers a convenient means to check your account balance. Simply log into RCC clusters via `ssh` and execute the following command:

``` 
accounts balance  
```

## How do I review the usage of my allocation?
The `accounts` tool provides several options for summarizing allocation usage. To obtain a summary, execute the command:

```
accounts usage
```

To view usage per job, utilize the following command:

```
accounts usage --byjob
```

If you are the PI, you may employ the `--byuser` option to view individual usage by group members:

```
accounts usage --byuser
```

---

*For additional details on account creation, visit the [accounts and allocations page](https://rcc.uchicago.edu/accounts-allocations) on our main website.*