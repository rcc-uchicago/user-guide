# Developer Tools

## Debuggers

On Midway3 [GDB](https://www.sourceware.org/gdb/documentation/){:target='_blank'} and <a href='https://valgrind.org/docs/manual/quick-start.html' target='_blank'>Valgrind</a> as modules for debugging and memory leak checking with your code.

To debug your code with `gdb`, you compile your code with `-g` and then run `gdb`:
```
g++ -g -o test test.cpp
module load gdb
gdb --args ./test param1 param2
```
You can also use `gdb` to debug your Python codes. Alternatively, use <a href='https://docs.python.org/3/library/pdb.html' target='_blank'>`pbd`.</a>

```
python3 -m pdb myscript.py
```
To check if there is any memory leak with your code, use `valgrind`
```
g++ -g -o test test.cpp
module load valgrind
valgrind --leak-check=full --track-origins=yes ./test param1 param2
```
Please refer to the official documentation of [GDB](https://www.sourceware.org/gdb/documentation/){:target='_blank'} and <a href='https://valgrind.org/docs/manual/quick-start.html' target='_blank'>Valgrind</a> for more information.

For CUDA codes, after loading the CUDA toolkit module (e.g. `module load cuda/12.2`) you can use `cuda-gdb` and `cuda-sanitizer`.


## Profilers

On Midway3 there are currently 3 profiling tools: [TAU](http://www.cs.uoregon.edu/research/tau/home.php), [NVIDIA Nsight](https://developer.nvidia.com/nsight-systems) and [Intel VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html).

[TAU](http://www.cs.uoregon.edu/research/tau/home.php){:target='_blank'} is a tool for profiling and tracing toolkit for performance
analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python. You can load `tau/2.31` on Midway3.

The TAU binaries and scripts in the subfolders `$TAU_HOME/bin`, and several `Makefile.*` in `$TAU_HOME/lib` .
To use TAU, you need to rebuild your code using one of the scripts inside `$TAU_HOME/bin`: C codes use `tau_cc.sh`; C++ codes use `tau_cxx.sh`
(see for example, the doc page at [OLCF](https://docs.olcf.ornl.gov/software/profiling/TAU.html){:target='_blank'}).
Should a new `Makefile.foo` be needed, then the `CC` and `CXX` environment variables need to be exported: 

```
export CC=tau_cc.sh CXX=tau_cxx.sh F90=tau_f90.sh
```
before the first `cmake` run, or before running `make`.

Run the generated binaries as usual (e.g. `mpirun -np 4 ./binary args`) the output will now include the files `profile.*` in the working directory.
At this point, run `paraprof` to launch the GUI analysis (need `module load java`), or `pprof` for command-line output.

Different options for compile time are available (e.g. `-optVerbose`), options for run time (e.g. `TAU_TRACK_MEMORY_LEAKS=1`)

[NVIDIA Nsight](https://developer.nvidia.com/nsight-systems) is a system-wide performance analysis tool designed to visualize an application’s algorithms, identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs.

To use NVIDIA Nsight System and Nsight Compute, load one of the available `cuda` modules.
```
module load cuda/12.2
```
To launch the corresponding GUI applications, use
```
nsys-ui
```
and
```
ncu-ui
```
You can also use the command-line interface `nsys` and `ncu`. Please refer to the [NVIDIA Nsight documentation](https://docs.nvidia.com/nsight-systems/index.html) for further details.

[Intel VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html) is part of the oneAPI(C) software suite for optimizing application performance, system performance, and system configuration for HPC.
To use the profilers, `vtune` and the GUI `vtune-gui`, in a [ThinLinc](../thinlinc/main.md) session, you load the `oneapi` module
```
module load oneapi/2024.2
vtune-gui
```
