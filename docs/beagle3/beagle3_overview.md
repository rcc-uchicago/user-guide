# Beagle3
<!-- From these links:
https://biologicalsciences.uchicago.edu/news/features/beagle-3-gpu-cluster -->

## What is Beagle3?
Beagle3 is a high-performance computing cluster funded by the NIH grant led by Professor Benoit Roux, the Amgen Professor of Biochemistry and Molecular Biology. [The project](https://biologicalsciences.uchicago.edu/news/features/beagle-3-gpu-cluster) benefits biomedical research with cutting-edge HPC resources for modeling and large-scale simulations of the molecular building blocks for biological functions. The cluster also serves research projects that employ recent advances in imaging technology, like cryo-electronic microscopy, for producing images of molecules at unprecedented resolution. The enormous amount of data rapidly generated need commensurate amounts of computing horsepower to analyze. Beagle3 has been in service since February 2022.

Beagle3 consists of 44 computing nodes, each with an 32-core Intel Xeon Gold 6346 CPUs and 4 NVIDIA A100 graphics processing units (GPUs).

## Gaining Access

You should contact your PI for access to Beagle3. You can also reach out to our Help Desk at [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu) for assistance.

## Partitions
=== "Beagle3"
      | Partition | Nodes  | CPUs | CPU Type  | GPUs | GPU Type| Total Memory| Time Limit |
      | --------- | -------| -----| --------- | ---- | ------- | ----------- | ---------- |
      | beagle3   |   22   |  32  | gold-6346 | 4    |  a40    |    256 GB   |  48:00:00  |
      | beagle3   |   22   |  32  | gold-6346 | 4    |  a100   |    256 GB   |  48:00:00  |
      | beagle3   |   4    |  32  | gold-6346 | None |  None   |    512 GB   |  48:00:00  |
      
## Connecting and Running Jobs

You connect to and run jobs on Beagle3 in a similar manner to [Midway](../midway23/midway_getting_started.md). Your home space is the same on Midway3, and you can access other mount points on Beagle3 from Midway3 as well.

## Troubleshooting

For further assistance, please contact our Help Desk at [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu).