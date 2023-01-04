# Message Passing Interface (MPI)

For more information on how to run MPI jobs on Midway see [MPI jobs](../../../running-jobs/mpi/index.md#mpi-jobs)

RCC supports the following MPI implementations:


* IntelMPI


* MVAPICH2


* OpenMPI

Each MPI implementation usually has a module available for use with GCC,
the Intel Compiler Suite, and PGI. Please see module_tag_high performance computing for the
list of available MPI modules.

## MPI Implementation Notes

The different MPI implementations have different options and features. Any
notable differences are noted here.

### IntelMPI

IntelMPI uses an environment variable to affect the network communication
fabric it uses:


### I_MPI_FABRICS()
During job launch the Slurm TaskProlog detects the network hardware and sets
this variable approately. This will typically be set to `shm:ofa`, which makes
IntelMPI use shared memory communication followed by ibverbs. If a job is run
on a node without Infiniband this will be set to `shm` which uses shared
memory only and limits IntelMPI to a single node job. This is usually what is
wanted on nodes without a high speed interconnect. This variable can be
overridden if desired in the submission script.

### MVAPICH2

MVAPICH2 is compiled with the **OFA-IB-CH3** interface. There is no support
for running programs compiled with MVAPICH2 on loosely coupled nodes.

GPUDirect builds of MVAPICH2 with CUDA enabled are available for use on the GPU
nodes. These builds are otherwise identical to the standard MVAPICH2 build.

### OpenMPI

Nothing at this time.
