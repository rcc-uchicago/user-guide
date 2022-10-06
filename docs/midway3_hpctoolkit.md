# HPC Toolkit

HPC Toolkit is an open source suite of profiling and performance analysis.  It
requires recompiling the code to be instrumented, but otherwise the code can remain
unchanged.

## Compile

Compile source files as normally using your normal compiler.  Prepend the command
**hpclink** to the linking stage and statically link:

```default
$ module load hpctoolkit
$ hpclink gcc -static -g foo.c
```

Or in the case of an MPI code:

```default
$ module load hpctoolkit/5.3+openmpi-1.6
$ hpclink mpicc -static -g <source>.c -o <executable>
```

Currently HPC Toolkit modules are created only for GNU compiler based MPI environments.

## Gather Sampling Data

The command **hpcrun** is used to run the instrumented program and collect
sampling data.  The option `-l` will list the available events that may be
pofiled, including those defined by [PAPI](../papi/index.md#papi). The user can control which events
are profiled and at what frequency using the option `-e`:

```default
$ hpcrun -e PAPI_L2_DCM@510011 <executable>
```

or:

```default
$ mpirun hpcrun -e PAPI_L2_DCM@510011 <executable>
```

Multiple events can be profiled in a single invokation of **hpcrun**, however
not all events are compatible.  It may also be necessary to run **hpcrun**
multiple times to gather sufficient events to capture relatively rare events.

## Statially Instrument Code

HPC Toolkit performs a static analysis of the programs original source in order
to properly interpret the sampling data.  Use the command **hpcstruct**:

```default
$ hpcstruct <executable>
```

## Correlate Source and Sampling Data

The **hpcprof** command collects all available samples and correlates them
with the static analysis produced by **hpcstruct**:

```default
$ hpcprof -I path-to-source -S <executable>.hpcstruct hpctoolkit-<executable>-measurements
```

## Analysis

Once the database of measurements has been created, a separate module is available
with a program to graphically visualize and explore the data:

```default
$ module load hpcviewer
$ hpcviewer hpctoolkit-<executable>-database
```
