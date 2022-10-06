# Valgrind

Valgrind is an open source set of debugging and profiling tools.  It is
most commonly used to locate memory errors, including leaks, but also can
be used to debug threaded codes and profile cache efficiency.

See the [Valgrind Online Documentation](http://valgrind.org/docs/manual/)
for more information.

## Usage

The following snippet shows how to load the valgrind module and use it to
perform analysis on a c code.

```bash
module load valgrind
gcc -g source.c
valgrind --tool=[memcheck,cachgrind,helgrind] ./a.out
```

If no tool is specified, valgrind will default to the memory checker.

### Memcheck

Memcheck is a tool to detect a wide range of memory errors including buffer over-runs,
memory leaks and double-freeing of heap blocks, and uninitialized variables.

Download `memleak.c`: for a simple example of using the cachegrind module to
identify a memory leak:

```default
$ module load valgrind
$ gcc -g memleak.c
$ valgrind --tool=memcheck ./a.out
==3153== Memcheck, a memory error detector
==3153== Copyright (C) 2002-2012, and GNU GPL'd, by Julian Seward et al.
==3153== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright info
==3153== Command: ./a.out
==3153==
==3153==
==3153== HEAP SUMMARY:
==3153==     in use at exit: 800 bytes in 10 blocks
==3153==   total heap usage: 10 allocs, 0 frees, 800 bytes allocated
==3153==
==3153== LEAK SUMMARY:
==3153==    definitely lost: 800 bytes in 10 blocks
==3153==    indirectly lost: 0 bytes in 0 blocks
==3153==      possibly lost: 0 bytes in 0 blocks
==3153==    still reachable: 0 bytes in 0 blocks
==3153==         suppressed: 0 bytes in 0 blocks
==3153== Rerun with --leak-check=full to see details of leaked memory
==3153==
==3153== For counts of detected and suppressed errors, rerun with: -v
==3153== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 6 from 6)
```

Running memcheck without any options identifies that 800 bytes were not
freed at the time the program terminated, and those were allocated in 10
distinct blocks.  To get a better idea of where those blocks were allocated,
use the option `--leak-check=full`:

```default
$ valgrind --tool=memcheck --leak-check=full ./a.out
==3154== Memcheck, a memory error detector
==3154== Copyright (C) 2002-2012, and GNU GPL'd, by Julian Seward et al.
==3154== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright info
==3154== Command: ./a.out
==3154==
==3154==
==3154== HEAP SUMMARY:
==3154==     in use at exit: 800 bytes in 10 blocks
==3154==   total heap usage: 10 allocs, 0 frees, 800 bytes allocated
==3154==
==3154== 800 bytes in 10 blocks are definitely lost in loss record 1 of 1
==3154==    at 0x4C278FE: malloc (vg_replace_malloc.c:270)
==3154==    by 0x400575: main (memleak.c:i24)
==3154==
==3154== LEAK SUMMARY:
==3154==    definitely lost: 800 bytes in 10 blocks
==3154==    indirectly lost: 0 bytes in 0 blocks
==3154==      possibly lost: 0 bytes in 0 blocks
==3154==    still reachable: 0 bytes in 0 blocks
==3154==         suppressed: 0 bytes in 0 blocks
==3154==
==3154== For counts of detected and suppressed errors, rerun with: -v
==3154== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 6 from 6)
```

Now memcheck has identified that the 10 code blocks were allocated at memleak.c
line 10, and the user can modify the code to free those allocations at the
appropriate place.

### Cachegrind

Cachegrind is a Valgrind tool that simulates (rather than measures) how a code interact with
the multi-level caches found in modern computer architectures.  It is very useful for identifying
cache misses as a performance problem, as well as identifying parts of the code responsible.
Cachegrind does have several limitations, and can dramatically increase the time it takes to
execute a code.  See the [cachgrind manual](http://valgrind.org/docs/manual/cg-manual.html)
for full details.

Download `matrixmult.c` for a simple example using the cachegrind module to estimate
cache efficiency:

```default
$ module load valgrind
$ gcc -g matrixmult.c
$ valgrind --tool=cachegrind ./a.out
==2548== Cachegrind, a cache and branch-prediction profiler
==2548== Copyright (C) 2002-2012, and GNU GPL'd, by Nicholas Nethercote et al.
==2548== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright info
==2548== Command: ./a.out
==2548==
--2548-- warning: L3 cache found, using its data for the LL simulation.
==2548==
==2548== I   refs:      3,252,178,387
==2548== I1  misses:              745
==2548== LLi misses:              738
==2548== I1  miss rate:          0.00%
==2548== LLi miss rate:          0.00%
==2548==
==2548== D   refs:      1,082,643,679  (720,139,382 rd   + 362,504,297 wr)
==2548== D1  misses:      406,465,246  (405,103,433 rd   +   1,361,813 wr)
==2548== LLd misses:          313,706  (      1,950 rd   +     311,756 wr)
==2548== D1  miss rate:          37.5% (       56.2%     +         0.3%  )
==2548== LLd miss rate:           0.0% (        0.0%     +         0.0%  )
==2548==
==2548== LL refs:         406,465,991  (405,104,178 rd   +   1,361,813 wr)
==2548== LL misses:           314,444  (      2,688 rd   +     311,756 wr)
==2548== LL miss rate:            0.0% (        0.0%     +         0.0%  )
```

The above output shows that the example code has a greater than 50% read cache miss rate,
which will significantly degrade performance.  Since the code was compiled with the
`-g` compiler flag, the cg_annotate tool can be used to parse cachgrind output
and produce a line-by-line annotated report:

```default
$ cg_annotate --auto=yes cachegrind.out.2548
--------------------------------------------------------------------------------
I1 cache:         32768 B, 64 B, 8-way associative
D1 cache:         32768 B, 64 B, 8-way associative
LL cache:         20971520 B, 64 B, 20-way associative
Command:          ./a.out
Data file:        cachegrind.out.2548
Events recorded:  Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Events shown:     Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Event sort order: Ir I1mr ILmr Dr D1mr DLmr Dw D1mw DLmw
Thresholds:       0.1 100 100 100 100 100 100 100 100
Include dirs:
User annotated:
Auto-annotation:  on

--------------------------------------------------------------------------------
           Ir I1mr ILmr          Dr        D1mr  DLmr          Dw      D1mw    DLmw
--------------------------------------------------------------------------------
3,252,178,387  745  738 720,139,382 405,103,433 1,950 362,504,297 1,361,813 311,756  PROGRAM TOTALS

--------------------------------------------------------------------------------
           Ir I1mr ILmr          Dr        D1mr DLmr          Dw      D1mw    DLmw  file:function
--------------------------------------------------------------------------------
3,251,974,540    6    6 720,090,005 405,100,952    0 362,490,010 1,361,251 311,250  /home/drudd/debug/matrixmult.c:main

--------------------------------------------------------------------------------
-- Auto-annotated source: /home/drudd/debug/matrixmult.c
--------------------------------------------------------------------------------
           Ir I1mr ILmr          Dr        D1mr DLmr          Dw      D1mw    DLmw

-- line 12 ----------------------------------------
            .    .    .           .           .    .           .         .       .   *******************************************************************/
            .    .    .           .           .    .           .         .       .  #include <stdlib.h>
            .    .    .           .           .    .           .         .       .  #include <stdio.h>
            .    .    .           .           .    .           .         .       .  #include <math.h>
            .    .    .           .           .    .           .         .       .
            .    .    .           .           .    .           .         .       .  #define N 300
            .    .    .           .           .    .           .         .       .  #define M 4000
            .    .    .           .           .    .           .         .       .
          909    0    0           0           0    0           3         0       0  int main( int argc, char *argv[] ) {
            .    .    .           .           .    .           .         .       .      int i, j, k;
            .    .    .           .           .    .           .         .       .      double *A, *B, *C;
            .    .    .           .           .    .           .         .       .      double tmp;
            .    .    .           .           .    .           .         .       .
            3    1    1           0           0    0           1         0       0      A = (double *)malloc(N*M*sizeof(double));
            3    0    0           0           0    0           1         0       0      B = (double *)malloc(N*M*sizeof(double));
            2    0    0           0           0    0           1         0       0      C = (double *)malloc(N*N*sizeof(double));
            .    .    .           .           .    .           .         .       .
            7    1    1           0           0    0           0         0       0      if ( A == NULL || B == NULL || C == NULL ) {
            .    .    .           .           .    .           .         .       .          fprintf(stderr,"Error allocating memory!\n");
            .    .    .           .           .    .           .         .       .          exit(1);
            .    .    .           .           .    .           .         .       .      }
            .    .    .           .           .    .           .         .       .
            .    .    .           .           .    .           .         .       .      /* initialize A & B */
        1,801    0    0           0           0    0           0         0       0      for ( i = 0; i < N; i++ ) {
    6,000,600    1    1           0           0    0           0         0       0          for ( j = 0; j < M; j++ ) {
    2,400,000    0    0           0           0    0   1,200,000   150,000 150,000              A[M*i+j] = 3.0;
    2,400,000    0    0           0           0    0   1,200,000 1,199,999 150,000              B[N*j+i] = 2.0;
            .    .    .           .           .    .           .         .       .          }
            .    .    .           .           .    .           .         .       .      }
            .    .    .           .           .    .           .         .       .
      180,001    0    0           0           0    0           0         0       0      for ( i = 0; i < N*N; i++ ) {
      180,000    0    0           0           0    0      90,000    11,251  11,250          C[i] = 0.0;
            .    .    .           .           .    .           .         .       .      }
            .    .    .           .           .    .           .         .       .
          600    0    0           0           0    0           0         0       0      for ( i = 0; i < N; i++ ) {
      630,600    2    2      90,000      11,251    0           0         0       0          for ( j = 0; j < N; j++ ) {
1,800,180,000    0    0           0           0    0           0         0       0              for ( k = 0; k < M; k++ ) {
1,440,000,000    0    0 720,000,000 405,089,701    0 360,000,000         0       0                  C[N*i+j] += A[M*i+k]*B[N*k+j];
            .    .    .           .           .    .           .         .       .              }
            .    .    .           .           .    .           .         .       .          }
            .    .    .           .           .    .           .         .       .      }
            .    .    .           .           .    .           .         .       .
            3    0    0           0           0    0           2         1       0      free(A);
            2    0    0           0           0    0           1         0       0      free(B);
            3    0    0           1           0    0           1         0       0      free(C);
            .    .    .           .           .    .           .         .       .
            .    .    .           .           .    .           .         .       .      return 0;
            6    1    1           4           0    0           0         0       0  }

--------------------------------------------------------------------------------
 Ir I1mr ILmr  Dr D1mr DLmr  Dw D1mw DLmw
--------------------------------------------------------------------------------
100    1    1 100  100    0 100  100  100  percentage of events annotated
```

Note that in this example the loop order causes very poor cache performance for the innermost line of the nested loop.  Exchanging
the k and j indexed loops will give significantly better performance.  Still better performance can be obtained through blocking,
or, as this is a standard linear algebra opperation, using LAPACK or the Intel Math Kernel Library, which has tuned routines for
performing such calculations.

### Helgrind

Helgrind is a thread error checking tool.  Unfortunately it has poor interaction with gcc’s OpenMP implementation, and can lead
to a large number of distracting messages.  Still, it can be useful in identifying races or unprotected critical sections within
shared memory parallel code.