# [LAMMPS](http://lammps.sandia.gov/)

## Table of Contents


* Quick Start


* Intro of LAMMPS


* Get Best Performance


* Benchmarks


* Copyright

## Quick Start

If you’re familiar with LAMMPS software, this section gives you quick steps of using LAMMPS, which has been
installed and optimized on the Midway cluster at RCC. LAMMPS is installed with RCC Module system. You can use either of the following commands to load it into the
shell environment:

```default
module load lammps
```

This module is built from the SVN source hosted at svn://svn.icms.temple.edu/lammps-ro/trunk, Version 30Sep14.
The SVN trunk provides the up-to-date code from LAMMPS developers. The optimiztion package “OPT” is compiled
along with this binary:

```default
module load lammps-plumed
```

This module is built from the TARBALL source hosted at [http://lammps.sandia.gov/download.html](http://lammps.sandia.gov/download.html), Version 5Sep14, which is the latest stable
distribution. There are two important features in this installation: (1) two packages USER-OMP and USER-INTEL were added for optimization;
(2) The offsite pakcage “USER-PLUMED” was added to provide free energy techniques.

After loading either of the two modules, you can run LAMMPS with the binary “lmp_intelmpi”. Although the two modules were compiled with different vesions of Intel MPI
libraries, the module system can automatically load the correct one. A typical SLURM script of running LAMMPS jobs is following:

```bash
#!/bin/sh

#SBATCH --job-name=lammps
#SBATCH --output=lammps-%j.out
#SBATCH --constraint=ib
#SBATCH --exclusive
#SBATCH --nodes=4

module load lammps
mpirun lmp_intelmpi < in.lj
```

GPU support has been also patched in lammps-plumed module. Two packages, GPU and USER-CUDE were compiled with CUDA-4.2. The module is named with suffix
with suffix of “-cuda” for you to load or use them:

```default
module load lammps-plumed/5Sep14-cuda+intelmpi-5.0+intel-15.0
mpirun lmp_intelmpi-cuda -c on -sf cuda < in.lj
```

## Intro of LAMMPS

LAMMPS is a simulation software for particle systems. It is specially designed for molecular dynamics technique and large-scalse parallel
simulations. It is an open-source code and developed and maintained by Sandia National Liboratory (SNL). It has been widely used for studies
of methodology & algorithm developments and simulations of material science, chemistry, physics and biology.

For more information of LAMMPS, please visit its offical website: [http://http//lammps.sandia.gov/](http://http//lammps.sandia.gov/)

To gain more advice of using LAMMPS efficiently, please read its discussion section on “Acceleration” at: [http://lammps.sandia.gov/doc/Section_accelerate.html](http://lammps.sandia.gov/doc/Section_accelerate.html)

## Get Best Performance

The module lammps-plumed is installed with following packages:

ASPHERE BODY    CLASS2  COLLOID DIPOLE  FLD     GRANULAR        MANYBODY        KSPACE  MC      MISC    MOLECULE        REPLICA
RIGID   SHOCK   SRD     USER-CG-CMM     USER-EFF        USER-FEP        USER-LB USER-MISC       USER-MOLFILE    USER-OMP        USER-SPH
USER-PLUMED     USER-INTEL

To know more information about these packages, please read [http://lammps.sandia.gov/doc/Section_start.html#start_3](http://lammps.sandia.gov/doc/Section_start.html#start_3) If you need other packages
to be installed in this module, please contact [yuxing@uchicago.edu](mailto:yuxing@uchicago.edu)

The binaries of LAMMPS compiled here are aim to provide RCC users the optimized solutions. Therefore, three important packages are specially
discussed here: OPT, USER-OMP and USER-INTEL.

### **OPT**

Quote from LAMMPS website: “*The OPT package was developed by James Fischer (High Performance Technologies), David Richie, and Vincent Natoli
(Stone Ridge Technologies). It contains a handful of pair styles whose compute() methods were rewritten in C++ templated form to reduce the
overhead due to if tests and other conditional code.*”

To use OPT acceleration, you just need to put “-sf opt” in your job command:

```default
Ex: lmp_intelmpi -sf opt < lj.in
```

However, only part of pair-styles are optimized in this package.

### **USER-OMP**

The USER-OMP package was developed by Axel Kohlmeyer at Temple University. The purpose of package is to introduce the OpenMP/MPI hybrid
parallel scheme into LAMMPS to gain benefits from the state-of-art multicore processors. Therefore, the parallel jobs are run in the
combination of **SMP threads** x **MPI tasks**.

For example, if you request the resource of 64 cores (4 nodes) on Sandyb partition through SLURM systems, you can choose different
combination (16x4, 8x8, 4x16, et al) to receive the optimal performace. To do this, please set the following options correctly. For example,
if I want to run 8 MPI tasks total, and each of them allocate 8 threads, which means one MPI task per Sandy-Bridge processor:

```default
--nnodes=4           // allocate 4 nodes total
--ntasks-per-node=2  // execute 2 MPI tasks per node (1 per processor)
--cpus-per-task=8    // allocate 8 openmp threads per MPI task
```

You can also set environment variable OMP_NUM_THREADS=8 for this. (Not neccessary)

Besides, you need to also turn on the OMP suffix in job command:

```default
Ex: lmp_intelmpi -sf omp < lj.in
```

At the beginning of the LAMMPS in-script (i.e., lj.in in this example), you need to also specify the loading of pacakge by:

```default
package omp $N
```

$N is the number of OMP threads, which equals to 8 in this example.

Unfortunately we didn’t a boost of speed on this hybrid code. For most of the cases, OMP_NUM_THREADS=1 gives the best performance,
which means hybrid isn’t actually used. **However, the USER-OMP pacakge did optimize lots of the codes, from different force calculations to
integrations, which results a significant acceleration although OMP_NUM_THREADS=1 is used.**

### **USER-INTEL**

This is a very new package that was developed by Intel technicians. The purpose of this pacakages is to implement the MIC support into
LAMMPS. However, without having a MIC card, the code can be also accelerated a lot on CPU-only clusters, because the codes were rewritten to
support the INTEL AVX vectoring tenchnique. USER-INTEL also provides a large number of optimized codes for LAMMPS functions.

To use OPT acceleration, you just need to put “-sf opt” in your job command:

```default
Ex: lmp_intelmpi -sf intel < lj.in
```

At the beginning of the LAMMPS in-script (i.e., lj.in in this example), you need to also specify the loading of pacakge by:

```default
package intel
```

## Benchmarks

Testing infomation:

```default
Hardware: Haswell E5-2660 v3. (2.6GHz, 20 core) DDR4, 2133MHz
System: Pure water box (100 x 100 x 100 A^3), 95,577 atoms
PPPM: double precision FFTW3, 1E-4
CUTOFF: 10A
Steps: 1000
```

| Timings

 | Plain

 | OPT

 | USER-OMP

 | USER-INTEL

 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------- | ---------- |  |  |  |  |  |  |  |  |  |  |
| Total

                                   | 50.07

                                                                                                                                                                                                                                                                                                                                               | 45.20

                                              | 41.41

           | 33.75

      |
| Pair

                                    | 37.55

                                                                                                                                                                                                                                                                                                                                               | 33.11

                                              | 29.07

           | 21.54

      |
| Kspace

                                  | 6.48

                                                                                                                                                                                                                                                                                                                                                | 6.86

                                               | 5.89

            | 5.75

       |
| Neighbor

                                | 3.18

                                                                                                                                                                                                                                                                                                                                                | 2.29

                                               | 3.08

            | 2.95

       |
| Communication

                           | 0.90

                                                                                                                                                                                                                                                                                                                                                | 0.85

                                               | 1.02

            | 1.01

       |
| Output

                                  | 0.01

                                                                                                                                                                                                                                                                                                                                                | 0.01

                                               | 0.01

            | 0.01

       |
| Other

                                   | 1.60

                                                                                                                                                                                                                                                                                                                                                | 1.76

                                               | 2.07

            | 2.12

       |
*Numbers are in seconds. Lower is better.*

## Copyright

To get the permission of using the content (text, images and benchmark data) of this document in anywhere else,
please send an Email to [yuxing@uchicago.edu](mailto:yuxing@uchicago.edu).
