# PAPI

PAPI is a multi-platform library for portably accessing hardware counters
for event profiling of software including flop counts, cache efficiency,
and branch prediction rates.

See the [PAPI website](http://icl.cs.utk.edu/papi/) for more information.

## Usage

The user must add PAPI function calls to their code and link to the PAPI library
in order to access the hardware counters.  Often PAPI calls can be added to previously
instrumented code through timing calls, otherwise the user will need to identify the
subset of the code to be profiled.

An example code that uses PAPI to identify poor cache performance is located below.

### Available Counters

The command **papi_avail** will determine which PAPI counters are accessible
on the current system.  Some counters are supported natively, and others can be derived
from other counters that are natively supported.  PAPI also supports multiplexing,
where a larger number of events can be profiled simultaneously using a sampling
technique.  See the PAPI documentation for more details.

**NOTE**: The number of active counters is much less than the number of counters available on
the system.  Sandy Bridge nodes have 11 registers that can be used for hardware counters,
but PAPI requires a few of those registers for internal functions.  In practice, ~4
independent PAPI events can be instrumented at one time, and valid combinations of
events must be found using trial-and-error.

```bash
$ module load papi/5.1
$ papi_avail -a
Available events and hardware information.
--------------------------------------------------------------------------------
PAPI Version             : 5.1.0.2
Vendor string and code   : GenuineIntel (1)
Model string and code    : Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (45)
CPU Revision             : 7.000000
CPUID Info               : Family: 6  Model: 45  Stepping: 7
CPU Max Megahertz        : 2599
CPU Min Megahertz        : 2599
Hdw Threads per core     : 2
Cores per Socket         : 8
NUMA Nodes               : 2
CPUs per Node            : 16
Total CPUs               : 32
Running in a VM          : no
Number Hardware Counters : 11
Max Multiplex Counters   : 64
--------------------------------------------------------------------------------

    Name        Code    Deriv Description (Note)
PAPI_L1_DCM  0x80000000  No   Level 1 data cache misses
PAPI_L1_ICM  0x80000001  No   Level 1 instruction cache misses
PAPI_L2_DCM  0x80000002  Yes  Level 2 data cache misses
PAPI_L2_ICM  0x80000003  No   Level 2 instruction cache misses
PAPI_L1_TCM  0x80000006  Yes  Level 1 cache misses
PAPI_L2_TCM  0x80000007  No   Level 2 cache misses
PAPI_L3_TCM  0x80000008  No   Level 3 cache misses
PAPI_TLB_DM  0x80000014  Yes  Data translation lookaside buffer misses
PAPI_TLB_IM  0x80000015  No   Instruction translation lookaside buffer misses
PAPI_L1_LDM  0x80000017  No   Level 1 load misses
PAPI_L1_STM  0x80000018  No   Level 1 store misses
PAPI_L2_STM  0x8000001a  No   Level 2 store misses
PAPI_STL_ICY 0x80000025  No   Cycles with no instruction issue
PAPI_BR_UCN  0x8000002a  Yes  Unconditional branch instructions
PAPI_BR_CN   0x8000002b  No   Conditional branch instructions
PAPI_BR_TKN  0x8000002c  Yes  Conditional branch instructions taken
PAPI_BR_NTK  0x8000002d  No   Conditional branch instructions not taken
PAPI_BR_MSP  0x8000002e  No   Conditional branch instructions mispredicted
PAPI_BR_PRC  0x8000002f  Yes  Conditional branch instructions correctly predicted
PAPI_TOT_INS 0x80000032  No   Instructions completed
PAPI_FP_INS  0x80000034  Yes  Floating point instructions
PAPI_LD_INS  0x80000035  No   Load instructions
PAPI_SR_INS  0x80000036  No   Store instructions
PAPI_BR_INS  0x80000037  No   Branch instructions
PAPI_TOT_CYC 0x8000003b  No   Total cycles
PAPI_L2_DCH  0x8000003f  Yes  Level 2 data cache hits
PAPI_L2_DCA  0x80000041  No   Level 2 data cache accesses
PAPI_L3_DCA  0x80000042  Yes  Level 3 data cache accesses
PAPI_L2_DCR  0x80000044  No   Level 2 data cache reads
PAPI_L3_DCR  0x80000045  No   Level 3 data cache reads
PAPI_L2_DCW  0x80000047  No   Level 2 data cache writes
PAPI_L3_DCW  0x80000048  No   Level 3 data cache writes
PAPI_L2_ICH  0x8000004a  No   Level 2 instruction cache hits
PAPI_L2_ICA  0x8000004d  No   Level 2 instruction cache accesses
PAPI_L3_ICA  0x8000004e  No   Level 3 instruction cache accesses
PAPI_L2_ICR  0x80000050  No   Level 2 instruction cache reads
PAPI_L3_ICR  0x80000051  No   Level 3 instruction cache reads
PAPI_L2_TCA  0x80000059  Yes  Level 2 total cache accesses
PAPI_L3_TCA  0x8000005a  No   Level 3 total cache accesses
PAPI_L2_TCR  0x8000005c  Yes  Level 2 total cache reads
PAPI_L3_TCR  0x8000005d  Yes  Level 3 total cache reads
PAPI_L2_TCW  0x8000005f  No   Level 2 total cache writes
PAPI_L3_TCW  0x80000060  No   Level 3 total cache writes
PAPI_FDV_INS 0x80000063  No   Floating point divide instructions
PAPI_FP_OPS  0x80000066  Yes  Floating point operations
PAPI_SP_OPS  0x80000067  Yes  Floating point operations; optimized to count scaled single precision vector operations
PAPI_DP_OPS  0x80000068  Yes  Floating point operations; optimized to count scaled double precision vector operations
PAPI_VEC_SP  0x80000069  Yes  Single precision vector/SIMD instructions
PAPI_VEC_DP  0x8000006a  Yes  Double precision vector/SIMD instructions
PAPI_REF_CYC 0x8000006b  No   Reference clock cycles
-------------------------------------------------------------------------
Of 50 available events, 17 are derived.

avail.c                                     PASSED
```

## Example

Download `matrixmult_papi.c` for an example using PAPI to measure the L2 cache miss
rate for a poorly-written matrix multiplication program:

```default
$ module load papi/5.1
$ gcc -O2 matrixmult_papi.c -lpapi
$ ./a.out
322761027 L2 cache misses (0.744% misses) in 5740137120 cycles
```

The precise output will vary with the system load.  Reversing the order of the inner two loops
should produce a significant improvement in cache efficiency and a corresponding speedup.
