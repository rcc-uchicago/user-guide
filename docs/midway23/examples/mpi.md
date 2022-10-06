# MPI jobs

Here we present a couple small examples illustrating how to use MPI
for distributed computing Midway. For more information on the MPI
libraries available on Midway, see [Message Passing Interface (MPI)](../../software/libraries/mpi/index.md#mpi-libraries).

Our main illustration is a “hello world” example. See file
`hellompi.c` for the C code we will compile and run.

```c
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[], char *envp[]) {
  int numprocs, rank, namelen;
  char processor_name[MPI_MAX_PROCESSOR_NAME];

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Get_processor_name(processor_name, &namelen);

  printf("Process %d on %s out of %d\n", rank, processor_name, numprocs);

  MPI_Finalize();
}

```

Copy `hellompi.c` to your home directory on Midway, load the
default OpenMPI module, and compile the program on a Midway login
node:

```default
module load openmpi
mpicc hellompi.c -o hellompi
```

`hellompi.sbatch` is a submission script that can be used to
submit a job to Midway to run the `hellompi` program:

```bash
#!/bin/bash

#SBATCH --job-name=hellompi
#SBATCH --output=hellompi.out
#SBATCH --ntasks=56
#SBATCH --partition=broadwl
#SBATCH --constraint=fdr

# Load the default OpenMPI module.
module load openmpi

# Run the hellompi program with mpirun. The -n flag is not required;
# mpirun will automatically figure out the best configuration from the
# Slurm environment variables.
 mpirun ./hellompi

```

Submit the MPI job to the Slurm job scheduler from a Midway login
node:

```default
sbatch hellompi.sbatch
```

Here is an example output:

```default
Process 1 on midway2-0172.rcc.local out of 56
Process 3 on midway2-0172.rcc.local out of 56
Process 5 on midway2-0172.rcc.local out of 56
Process 7 on midway2-0172.rcc.local out of 56
Process 6 on midway2-0172.rcc.local out of 56
Process 9 on midway2-0172.rcc.local out of 56
Process 10 on midway2-0172.rcc.local out of 56
Process 11 on midway2-0172.rcc.local out of 56
Process 13 on midway2-0172.rcc.local out of 56
Process 0 on midway2-0172.rcc.local out of 56
Process 2 on midway2-0172.rcc.local out of 56
Process 4 on midway2-0172.rcc.local out of 56
Process 8 on midway2-0172.rcc.local out of 56
Process 12 on midway2-0172.rcc.local out of 56
Process 17 on midway2-0173.rcc.local out of 56
Process 19 on midway2-0173.rcc.local out of 56
Process 21 on midway2-0173.rcc.local out of 56
Process 28 on midway2-0173.rcc.local out of 56
Process 29 on midway2-0173.rcc.local out of 56
Process 31 on midway2-0173.rcc.local out of 56
Process 32 on midway2-0173.rcc.local out of 56
Process 15 on midway2-0173.rcc.local out of 56
Process 18 on midway2-0173.rcc.local out of 56
Process 20 on midway2-0173.rcc.local out of 56
Process 22 on midway2-0173.rcc.local out of 56
Process 23 on midway2-0173.rcc.local out of 56
Process 24 on midway2-0173.rcc.local out of 56
Process 52 on midway2-0175.rcc.local out of 56
Process 25 on midway2-0173.rcc.local out of 56
Process 53 on midway2-0175.rcc.local out of 56
Process 26 on midway2-0173.rcc.local out of 56
Process 54 on midway2-0175.rcc.local out of 56
Process 27 on midway2-0173.rcc.local out of 56
Process 55 on midway2-0175.rcc.local out of 56
Process 14 on midway2-0173.rcc.local out of 56
Process 16 on midway2-0173.rcc.local out of 56
Process 30 on midway2-0173.rcc.local out of 56
Process 43 on midway2-0174.rcc.local out of 56
Process 51 on midway2-0174.rcc.local out of 56
Process 48 on midway2-0174.rcc.local out of 56
Process 49 on midway2-0174.rcc.local out of 56
Process 46 on midway2-0174.rcc.local out of 56
Process 44 on midway2-0174.rcc.local out of 56
Process 45 on midway2-0174.rcc.local out of 56
Process 40 on midway2-0174.rcc.local out of 56
Process 42 on midway2-0174.rcc.local out of 56
Process 36 on midway2-0174.rcc.local out of 56
Process 37 on midway2-0174.rcc.local out of 56
Process 47 on midway2-0174.rcc.local out of 56
Process 34 on midway2-0174.rcc.local out of 56
Process 38 on midway2-0174.rcc.local out of 56
Process 35 on midway2-0174.rcc.local out of 56
Process 39 on midway2-0174.rcc.local out of 56
Process 41 on midway2-0174.rcc.local out of 56
Process 50 on midway2-0174.rcc.local out of 56
Process 33 on midway2-0174.rcc.local out of 56
```

From this output, we observe that the computation is distributed on 4
different nodes, with many threads running simultaneously on the same
node.

When developing your own sbatch script for MPI-based computations,
keep in mind the following points.

Without the `--constraint=fdr` or `--constraint=edr`
options, your computations may run on nodes with FDR, EDR, or
combination of both.

It is possible to control the number of tasks that are run per node
with the `--ntasks-per-node` option. For example, submitting
the job like this to Midway:

```default
sbatch --ntasks-per-node=1 hellompi.sbatch
```

results in each thread running on a different node:

```default
Process 52 on midway2-0175.rcc.local out of 56 
Process 50 on midway2-0173.rcc.local out of 56
Process 49 on midway2-0172.rcc.local out of 56
Process 0 on midway2-0002.rcc.local out of 56
Process 13 on midway2-0052.rcc.local out of 56
Process 2 on midway2-0013.rcc.local out of 56
Process 9 on midway2-0033.rcc.local out of 56
Process 54 on midway2-0177.rcc.local out of 56
Process 53 on midway2-0176.rcc.local out of 56
Process 44 on midway2-0157.rcc.local out of 56
Process 55 on midway2-0178.rcc.local out of 56
Process 11 on midway2-0041.rcc.local out of 56
Process 40 on midway2-0152.rcc.local out of 56
Process 43 on midway2-0156.rcc.local out of 56
Process 45 on midway2-0161.rcc.local out of 56
Process 46 on midway2-0162.rcc.local out of 56
Process 38 on midway2-0147.rcc.local out of 56
Process 39 on midway2-0148.rcc.local out of 56
Process 24 on midway2-0101.rcc.local out of 56
Process 3 on midway2-0014.rcc.local out of 56
Process 42 on midway2-0155.rcc.local out of 56
Process 51 on midway2-0174.rcc.local out of 56
Process 36 on midway2-0145.rcc.local out of 56  
Process 25 on midway2-0102.rcc.local out of 56
Process 16 on midway2-0055.rcc.local out of 56
Process 18 on midway2-0057.rcc.local out of 56
Process 12 on midway2-0051.rcc.local out of 56
Process 14 on midway2-0053.rcc.local out of 56
Process 4 on midway2-0015.rcc.local out of 56
Process 15 on midway2-0054.rcc.local out of 56
Process 48 on midway2-0164.rcc.local out of 56
Process 28 on midway2-0105.rcc.local out of 56
Process 22 on midway2-0097.rcc.local out of 56
Process 30 on midway2-0118.rcc.local out of 56
Process 1 on midway2-0012.rcc.local out of 56
Process 35 on midway2-0144.rcc.local out of 56
Process 17 on midway2-0056.rcc.local out of 56
Process 37 on midway2-0146.rcc.local out of 56
Process 32 on midway2-0141.rcc.local out of 56
Process 34 on midway2-0143.rcc.local out of 56
Process 27 on midway2-0104.rcc.local out of 56
Process 31 on midway2-0119.rcc.local out of 56  
Process 29 on midway2-0106.rcc.local out of 56
Process 10 on midway2-0034.rcc.local out of 56
Process 47 on midway2-0163.rcc.local out of 56
Process 33 on midway2-0142.rcc.local out of 56
Process 26 on midway2-0103.rcc.local out of 56
Process 7 on midway2-0019.rcc.local out of 56
Process 20 on midway2-0073.rcc.local out of 56
Process 5 on midway2-0016.rcc.local out of 56
Process 8 on midway2-0027.rcc.local out of 56
Process 41 on midway2-0153.rcc.local out of 56
Process 6 on midway2-0017.rcc.local out of 56
Process 21 on midway2-0096.rcc.local out of 56
Process 19 on midway2-0072.rcc.local out of 56
Process 23 on midway2-0100.rcc.local out of 56
```

## Additional notes

Both OpenMPI and IntelMPI have the ability to launch MPI programs
directly with the Slurm command **srun**. It is not necessary to use this mode for most jobs, but it may provide additional job
launch options. For example, from a Midway login node it is possible
to launch the above `hellompi` program using OpenMPI using 28
MPI processes:

```default
srun -n28 hellompi
```

With IntelMPI, you need to also set an environment variable for this
to work:

```default
export I_MPI_PMI_LIBRARY=/software/slurm-current-$DISTARCH/lib/libpmi.so
srun -n28 hellompi
```                                                                      