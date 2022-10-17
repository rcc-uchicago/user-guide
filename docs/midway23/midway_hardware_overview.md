# Hardware Overview
The information here describes the hardware available on the Midway 2 and Midway 3 compute clusters.

## Midway 2
From these links:
https://rcc.uchicago.edu/resources/high-performance-computing

Midway 2, a professionally-managed high performance computing cluster forms the second generation core of RCC’s advanced computational infrastructure.

The types of CPU architectures RCC maintains are:

- Intel Broadwell—28 cores @ 2.4 GHz with 64 GB memory per node
- Intel Skylake—40 cores @ 2.4 GHz with 96 GB memory per node

The RCC also maintains a number of specialty nodes:

- Large shared memory nodes—up to 1TB of memory per node with either 16, 28, or 32 Intel CPU cores.
- 16,016 cores across 572 nodes
- 2.2 PB of storage.



## Midway 3
From these links:
https://mdw3-docs.rcc.uchicago.edu/

Midway3 is the latest high performance computing (HPC) cluster built, deployed and maintained by RCC.

At this time, only the Intel specific resources are made available. The key features of the Midway3 Intel hardware are listed as follows:

- 220 nodes total (10,560 cores)
- 210 standard compute nodes
- 2 big memory nodes (1x768GB and 1x1.52TB)
- 11 GPU nodes
- All nodes have HDR InfiniBand (100 Gbps) network cards.
- Each node has 960 GB SSD local disk
- Operating System throughout cluster is Centos 8

### GPU Nodes
There are 11 GPU nodes that are part of the Midway3 communal resources. Each GPU node has the Standard Intel Compute Node specifications and the following GPU configurations:

- 5 GPU nodes w/ 4x NVIDIA V100 GPUs per node
- 5 GPU nodes w/ 4x NVIDIA Quadro RTX 6000 GPUs per node
- 1 GPU node w/ 4x NVIDIA A100 GPUs per node

![GPUs](img/gpu.png)

### Big Memory Nodes
There are 2 big memory nodes available to all users. The big memory node has the Standard Intel Compute Node specifications, but with the following larger memory configurations:

- 1 nodes w/ 768 GB of memory
- 1 nodes w/ 1.52 TB of memory

### File Systems
There is a total of 2.2 PB of raw parallel file storage (1.7PB usable) that is part of the Midway3 cluster. Both file systems store their file metadata on a storage controller built of solid state drives, which overall will improve the responsiveness of each file system. Furthermore, the new storage system is designed that any file that is smaller than 4 KB in size will be bundled with the file metadata and stored on the pool of dedicated metadata SSDs that are part of the parallel storage system. This can lead to considerable improvement in performance for small file size (< 4 KB) I/O. This feature was not available with the Midway2 storage system as the metadata and data were both stored on slower mechanical hard drives.