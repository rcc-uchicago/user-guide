# Compilers

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

???+ note
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

## OpenMP

To compile your code with OpenMP, you just need to add to the compiling flags `-fopenmp` for GCC and AMD compilers and `-qopenmp` for Intel compilers.

## MPI

To compile your code with MPI, you need to load the MPI modules that are available.

=== "Midway2"
      | Vendor |  Module | Language      | Wrapper        |
      | -------| --------| -----------   |  -------------- |
      | OpenMPI    | `openmpi`   | C <br>C++<br>Fortran  | `mpicc`<br>`mpicxx`<br>`mpif90` |
      | MPICH    | `mpich`   | C <br>C++<br>Fortran  | `mpicc`<br>`mpicxx`<br>`mpif90` |
      | Intel  | `intelmpi`<br>oneaapi | C <br>C++<br>Fortran  | `mpiicc`<br>`mpiicpc`<br>`mpiifort` |
===+ "Midway3"
      | Vendor |  Module | Language      | Wrapper        |
      | -------| --------| -----------   |  -------------- |
      | OpenMPI    | `openmpi`   | C <br>C++<br>Fortran  | `mpicc`<br>`mpicxx`<br>`mpif90` |
      | MPICH    | `mpich`   | C <br>C++<br>Fortran  | `mpicc`<br>`mpicxx`<br>`mpif90` |
      | Intel  | `intelmpi` | C <br>C++<br>Fortran  | `mpiicc`<br>`mpiicpc`<br>`mpiifort` |
      | AMD    | `aocc`  | C <br>C++         | `clang`<br>`clang++`   |

???+ note
    Experienced users can build the MPI libraries of their preferences in their own space using the provided compilers above.


## CUDA

There are several [NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit) toolkit versions on Midway2 and Midway3. You can check the version provided with `module avail cuda`. On Midway3 there are currently 4 versions:

```
--------------------------- /software/modulefiles -----------------------------
cuda/10.2  cuda/11.2  cuda/11.3  cuda/11.5  
```
The current version of the GPU driver on the GPU nodes supports all the above CUDA toolkit versions.



