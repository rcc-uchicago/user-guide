# Compilers

In addition to having access to the provided software modules, you can always
compile and use your codes or other open-source codes on Midway. You can check out
the source files from GitHub (via ` git clone`) or copy from your local machine
to your own space on Midway (e.g. under `/home` or `/project`).

Depending on the requirements of the codes, you can load the compilers and libraries
that are provided as modules.

GNU GCC, Intel and AMD compilers are provided through modules on Midway2 and Midway3. The table below lists details about each of the module-provided compilers.

=== "Midway2"
      | Vendor |  Module | Language      | Compiler        |
      | -------| --------| -----------   |  -------------- |
      | GNU    | `gcc`   | C <br>C++<br>Fortran  | `gcc`<br>`g++`<br>`gfortran` |
      | Intel  | `intel` | C <br>C++<br>Fortran  | `icc`<br>`icpc`<br>`ifort` |
===+ "Midway3"
      | Vendor |  Module | Language      | Compiler        |
      | -------| --------| -----------   |  -------------- |
      | GNU    | `gcc`   | C <br>C++<br>Fortran  | `gcc`<br>`g++`<br>`gfortran` |
      | Intel  | `intel` | C <br>C++<br>Fortran  | `icc`<br>`icpc`<br>`ifort` |
      | AMD    | `aocc`  | C <br>C++         | `clang`<br>`clang++`   |
      | NVIDIA | `nvhpc` | C <br>C++<br>Fortran         | `nvc`<br>`nvc++`<br>`nvfortran` |

!!! note
    AMD compilers are available on the Midway3 AMD cluster and with `module use /software/modulefiles-amd`.

Each module may have different versions. The default version is always loaded if you do not specify explicitly with `module load`.
You should check with `module avail` to see what versions are available. For example, on Midway3 `module avail gcc` will return

```
---------------------------- /software/modulefiles -----------------------------
gcc/7.4.0  gcc/10.2.0(default) 
```
and `module avail intel`
```
---------------------------- /software/modulefiles -----------------------------
intel/16.0               
intel/18.0.5             
intel/19.1.1(default)
intel/2022.0
```
You can check the changes to the environment variables made by a particular module by the `module show` command.

## Multithreading with OpenMP

To compile your code or software packages that support multithreading with OpenMP, you just need to add to the compiling flags `-fopenmp` for GCC and AMD compilers and `-qopenmp` for Intel compilers.

## Message-passing interface (MPI)

To compile your code or software packages with MPI, you need to load the MPI modules that are available.
The list of libraries and software suites that provide MPI libraries is given as below.

=== "Midway2"
      | Library | Module                | Language             | Wrapper                             |
      |---------|-----------------------|----------------------|-------------------------------------|
      | OpenMPI | `openmpi`             | C <br>C++<br>Fortran | `mpicc`<br>`mpicxx`<br>`mpif90`     |
      | MPICH   | `mpich`               | C <br>C++<br>Fortran | `mpicc`<br>`mpicxx`<br>`mpif90`     |
      | Intel   | `intelmpi`<br>oneaapi | C <br>C++<br>Fortran | `mpiicc`<br>`mpiicpc`<br>`mpiifort` |
===+ "Midway3"
      | Library | Module     | Language             | Wrapper                             |
      |---------|------------|----------------------|-------------------------------------|
      | OpenMPI | `openmpi`  | C <br>C++<br>Fortran | `mpicc`<br>`mpicxx`<br>`mpif90`     |
      | MPICH   | `mpich`    | C <br>C++<br>Fortran | `mpicc`<br>`mpicxx`<br>`mpif90`     |
      | Intel   | `intelmpi` | C <br>C++<br>Fortran | `mpiicc`<br>`mpiicpc`<br>`mpiifort` |
      | AMD     | `aocc`     | C <br>C++            | `clang`<br>`clang++`                |
      | NVIDIA  | `nvhpc`    | C <br>C++<br>Fortran | `nvc`<br>`nvc++`<br>`nvfortran`     |

!!! note
    Experienced users can build the MPI libraries of their preferences in their own space using the provided compilers above.

## GPU codes

To compile GPU codes, you can use NVIDIA CUDA Toolkit and HPC SDK, or Intel OneAPI.

### NVIDIA toolsets

#### CUDA Toolkit

There are several [NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit) toolkit versions on Midway2 and Midway3. You can check the version provided with `module avail cuda`. On Midway3 there are several CUDA versions:

```
--------------------------- /software/modulefiles -----------------------------
cuda/10.2  cuda/11.2  cuda/11.3  cuda/11.5 cuda/11.7 cuda/12.0 
```
The current version of the GPU driver on the GPU nodes supports all the above CUDA toolkit versions. You can check the GPU driver version via the `nvidia-smi` command after loading a `cuda` module.

!!! note
     Although you can compile your CUDA code on the login node with the CUDA toolkit module loaded,
     running the generated binary on the login node will fail because there is no GPU on the login node.

#### NVIDIA HPC SDK

Another way to compile GPU-enabled C/C++/Fortran codes is to use compilers that support OpenACC. These compilers are available through the `nvhpc` module.
```
module load nvhpc
```
and check for the location of the compilers
```
which nvc++
which nvfortran
```
### Intel oneAPI

The [DPC++ Compiler](https://intel.github.io/llvm-docs/GetStartedGuide.html) compiles C++ and SYCL* source files with code for both CPU and a wide range of compute accelerators such as GPU and FPGA. You can load the `oneapi` module on Midway2 to get access to this compiler:
```
module load oneapi
```
and remember to source the shell script to setup the necessary environment variables:
```
source /software/oneapi-2021.beta7-el7-x86_64/inteloneapi/setvars.sh
```
and check for the location of the compilers
```
which dpcpp
```
## Go

[Go](https://go.dev/) is an open-source compiled programming language that gain an rapidly increasing interest and usage by the industry.  Although Go is not a traditional compiler, we include it here for convenience.
You can load Go as a module on Midway3.

## Java

Java is available as modules on Midway2 and Midway3. You can check the available modules via `module avail java`.