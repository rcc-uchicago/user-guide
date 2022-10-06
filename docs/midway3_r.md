# R

R is an interactive environment for computing.

To find the list of currently available R modules, run:

```default
$ module avail R
```

The RStudio IDE is also available as the `rstudio` module. This provides
a graphical interface for developing and running R. To use R in this mode,
we recommend connecting to the RCC cluster using [Connecting with ThinLinc](../../../connecting/index.md#thinlinc).

**NOTE:** Some of the examples below have not been revised to reflect
updates to the software and hardware on the RCC cluster. If an example
does not work, or if you have questions about an example, please
contact the RCC Help Desk for guidance.

## Serial Examples

Here is a simple “hello world” example to submit an R job to the SLURM
queue. This is appropriate for an R job that expects to use a single
CPU.

sbatch script `Rhello.sbatch`

```bash
#!/bin/sh

#SBATCH --partition=broadwl
#SBATCH --tasks=1

# Load the default version of hello.
module load R

# Use R CMD BATCH to run Rhello.R.
R CMD BATCH --no-save --no-restore Rhello.R
```

R script `Rhello.R`:

```default
print("Hello World")
```

## Parallel Examples

For parallel computing there are several options depending on whether
there should be parallel tasks on a single node only or multiple nodes
and the level of flexibility required. There are other R packages
available for parallel programming than what is covered here, but
we’ll cover some frequently used packages.

### Multicore

On a single node, it is possible to use doParallel and foreach.

sbatch script `doParallel.sbatch`:

```bash
#!/bin/bash

#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16

# --ntasks-per-node will be used in doParallel.R to specify the number
# of cores to use on the machine. Using 16 will allow us to use all
# cores on a sandyb node
module load R

R CMD BATCH --no-save --no-restore doParallel.R

```

R script `doParallel.R`:

```default
library(doParallel)

# use the environment variable SLURM_NTASKS_PER_NODE to set the number of cores
registerDoParallel(cores=(Sys.getenv("SLURM_NTASKS_PER_NODE")))

# Bootstrapping iteration example
x <- iris[which(iris[,5] != "setosa"), c(1,5)]
iterations <- 10000 # Number of iterations to run

# Parallel version of code
# Note the '%dopar%' instruction
parallel_time <- system.time({
  r <- foreach(icount(iterations), .combine=cbind) %dopar% {
    ind <- sample(100, 100, replace=TRUE)
    result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
    coefficients(result1)
  }
})

# Shows the number of Parallel Workers to be used
getDoParWorkers()

# Prints the total compute time.
parallel_time["elapsed"]
```

Output:

```default
Loading required package: foreach
Loading required package: iterators
Loading required package: parallel
[1] "16"
elapsed
  5.157
```

### SNOW

For multiple nodes, you can use the SNOW package, which provides a
select number of functions to simplify using multi-node
clusters. (NOTE OF CAUTION: This example may not work as described. In
particular, the workers may not actually run on 4 separate nodes.)

sbatch script `snow-test.sbatch`:

```bash
#!/bin/bash

#SBATCH --job-name=snow-test
#SBATCH --partition=broadwl
#SBATCH --nodes=4
#SBATCH --time=10
#SBATCH --exclusive

module load R

# the openmpi module is not loaded by default with R
module load openmpi/3.0.0

# Always use -n 1 for the snow package. It uses Rmpi internally to spawn
# additional processes dynamically
mpirun -np 1 R CMD BATCH --no-save --no-restore snow-test.R

```

R script `snow-test.R`:

```default
##
# Source: http://www.umbc.edu/hpcf/resources-tara/how-to-run-R.html
# filename: snow-test.R
#
# SNOW quick ref: http://www.sfu.ca/~sblay/R/snow.html
#
# Notes:
#   - Library loading order matters
#   - system.time([function]) is an easy way to test optimizations
#   - parApply is snow parallel version of 'apply'
#
##

library(Rmpi)
library(snow)

# Initialize SNOW using MPI communication. The first line will get the
# number of MPI processes the scheduler assigned to us. Everything
# else is standard SNOW
np      <- 4
cluster <- makeMPIcluster(np)

# Print the hostname for each cluster member
sayhello <- function() {
  info <- Sys.info()[c("nodename", "machine")]
  paste("Hello from", info[1], "with CPU type", info[2])
}

names <- clusterCall(cluster, sayhello)
print(unlist(names))

# Compute row sums in parallel using all processes, then a grand sum
# at the end on the master process
parallelSum <- function(m, n) {
  A <- matrix(rnorm(m*n), nrow = m, ncol = n)
  # Parallelize the summation
  row.sums <- parApply(cluster, A, 1, sum)
  print(sum(row.sums))
}

# Run the operation over different size matricies
system.time(parallelSum(5000, 5000))

# Always stop your cluster and exit MPI to ensure resources are
# properly freed.
stopCluster(cluster)
mpi.exit()
```

Output (trimmed for readability):

```default
        64 slaves are spawned successfully. 0 failed.
 [1] "Hello from midway197 with CPU type x86_64"
 [2] "Hello from midway197 with CPU type x86_64"
 [3] "Hello from midway197 with CPU type x86_64"
...
[63] "Hello from midway200 with CPU type x86_64"
[64] "Hello from midway197 with CPU type x86_64"
[1] -9363.914
   user  system elapsed
  3.988   0.443   5.553
[1] 1
[1] "Detaching Rmpi. Rmpi cannot be used unless relaunching R."
```

### Rmpi

For multiple nodes, you can also use Rmpi. This is what snow uses internally.
It is less convenient than snow, but also more flexible.

This page has a number of useful Rmpi examples: [http://www.umbc.edu/hpcf/resources-tara-2010/how-to-run-R.php](http://www.umbc.edu/hpcf/resources-tara-2010/how-to-run-R.php)

sbatch script `Rmpi.sbatch`:

```bash
#!/bin/sh

#SBATCH --partition=broadwl
#SBATCH --nodes=4
#SBATCH --time=1
#SBATCH --exclusive

module load R

# The openmpi module is not loaded by default with R.
module load openmpi/3.0.0

# Always use -n 1 for the Rmpi package. It spawns additional processes
# dynamically
mpirun -n 1 R CMD BATCH --no-save --no-restore Rmpi.R

```

R script `Rmpi.R`:

```default
library(Rmpi)

# initialize an Rmpi environment
ns <- 4
mpi.spawn.Rslaves(nslaves=ns)

# send these commands to the slaves
mpi.bcast.cmd( id <- mpi.comm.rank() )
mpi.bcast.cmd( ns <- mpi.comm.size() )
mpi.bcast.cmd( host <- mpi.get.processor.name() )

# all slaves execute this command
mpi.remote.exec(paste("I am", id, "of", ns, "running on", host))

# close down the Rmpi environment
mpi.close.Rslaves(dellog = FALSE)
mpi.exit()

```

Output (trimmed for readability):

```default
        64 slaves are spawned successfully. 0 failed.
master  (rank 0 , comm 1) of size 65 is running on: midway449
slave1  (rank 1 , comm 1) of size 65 is running on: midway449
slave2  (rank 2 , comm 1) of size 65 is running on: midway449
slave3  (rank 3 , comm 1) of size 65 is running on: midway449
... ... ...
slave63 (rank 63, comm 1) of size 65 is running on: midway452
slave64 (rank 64, comm 1) of size 65 is running on: midway449
$slave1
[1] "I am 1 of 65"

$slave2
[1] "I am 2 of 65"

...

$slave63
[1] "I am 63 of 65"

$slave64
[1] "I am 64 of 65"

```
