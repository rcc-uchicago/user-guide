# FFTW

FFTW, “the Fastest Fourier Transform in the West,” is a popular
open-source library for computing discrete Fourier transforms.  It
supports both real and complex transformations, in both single
and double precision.

RCC has configured and installed a large variety of fftw modules
including different versions, compiler choices, and parallelization
strategy.  Please contact RCC if a different version or configuration
is necessary for your work.

## FFTW2

FFTW 2.1.5 is an older, now unsupported version, but still commonly
used by codes as the API has changed in later versions.  The versions
compiled by the RCC support shared memory parallelism through OpenMP
and distributed parallelism through MPI.

See [FFTW2 Documentation](http://www.fftw.org/fftw2_doc) for complete documentation of this
version.

The non-MPI modules include both single and double precision versions,
as well as openMP support.  These have been built for all three RCC
supported compilers (gcc, intel, and pgi).  The library defaults to
double-precision, however single-precision can be used by adding
the prefix `s` to all filenames and library calls (see [the following](http://www.fftw.org/fftw2_doc/fftw_6.html#SEC69))
for more details).

The MPI modules are compiled for each MPI library and compiler
(leading to a large number of available combinations).  These should
all be interchangeable, simply ensure you match the correct module
to the MPI library and compiler you are using (the module system
will complain otherwise).

Each module adds the fftw2 library to your includes path, but for
codes that prefer to self-configure, the environment variable
`FFTW2_DIR` points to the currently loaded version.

The RCC help system includes a sample code to perform 1-dimensional
complex transformations in serial or in parallel.  To compile and
run each sample code, use the following commands:

`fftw2_serial.c`:

```bash
module load fftw2/2.1.5
gcc fftw2_serial.c -lm -lfftw
./a.out 512
```

`fftw2_openmp.c`:

```bash
module load fftw2/2.1.5
gcc -fopenmp fftw2_openmp.c -lm -lfftw -lfftw_threads
OMP_NUM_THREADS=8 ./a.out 512 8
```

`fftw2_mpi.c`:

```bash
module load openmpi/1.6
module load fftw2/2.1.5+openmpi-1.6
mpicc fftw2_mpi.c -lfftw_mpi -lfftw
mpirun -np 4 ./a.out 512
```

## FFTW3

The API for FFTW has significantly changed in the 3.X branch of FFTW.
MPI support has only recently been re-included as a stable feature
(3.3.X), and it is this version the RCC supports. As FFTW2 is no longer
supported, we recommend users upgrade to the newest version if their
code allows.

Documentation for this version can be viewed at:
[FFTW3 Documentation](http://fftw.org/fftw3_doc/)

Single precision support is included by post-fixing ‘f’ to commands and
filenames, see [this document](http://fftw.org/fftw3_doc/Precision.html)

Sample codes for serial, shared memory (openMP), and distributed (MPI)
have been included in the RCC help system.  Use the following to compile
and run each sample:

`fftw3_serial.c`:

```bash
module load fftw3/3.3
gcc fftw3_serial.c -lm -lfftw
./a.out 512
```

`fftw3_openmp.c`:

```bash
module load fftw3/3.3
gcc -fopenmp fftw3_openmp.c -lfftw3_omp -lfftw3 -lm
OMP_NUM_THREADS=8 ./a.out 512
```

`fftw3_threads.c`: (this is a pthread enabled version)

```bash
module load fftw3/3.3
gcc fftw3_threads.c -lpthread -lfftw3_threads -lfftw3 -lm
./a.out 512 8
```

`fftw3_mpi.c`: (note, only 2d or higher dimensional transforms supported in 3.3)

```bash
module load fftw3/3.3+openmpi-1.6
mpicc fftw3_mpi.c -lfftw3_mpi -lfftw3
mpirun -np 4 ./a.out 512
```
