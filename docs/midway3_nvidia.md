# CUDA and OpenACC Compilers

This page contains information about compiling GPU-based codes with NVidia’s CUDA compiler and PGI’s OpenACC compiler directives.  For information on how to run GPU Computing jobs in Midway, see [GPU jobs](../../../running-jobs/gpu/index.md#gpu-computing)

## Compiling CUDA GPU code on Midway

To view available CUDA versions on Midway, use the command:

```bash
module avail cuda
```

At time of writing, the available CUDA versions are:

```default
cuda/4.2(default)
cuda/5.0
cuda/5.5
```

A very basic CUDA example code is provided below `cudamemset.cu`:

```bash
#include <stdio.h>
#include <cuda.h>

int main(){

        int n = 16;

        // host and device memory pointers
        int *h_a;
        int *d_a;

        // allocate host memory
        h_a = (int*)malloc(n * sizeof(int));

        // allocate device memory
        cudaMalloc((void**)&d_a, n * sizeof(int));

        // set device memory to all zero's
        cudaMemset(d_a, 0, n * sizeof(int));

        // copy device memory back to host
        cudaMemcpy(h_a, d_a, n * sizeof(int), cudaMemcpyDeviceToHost);

        // print host memory
        for (int i = 0; i < n; i++){
                printf("%d ", h_a[i]);
        }
        printf("\n");

        // free buffers
        free(h_a);
        cudaFree(d_a);

        return 0;

}
```

CUDA code must be compiled with Nvidia’s nvcc compiler which is part of the cuda software module.  To build a CUDA executable, first load the desired CUDA module and compile with:

```bash
nvcc source_code.cu
```

## Compiling OpenACC GPU code on Midway

OpenACC is supported on Midway through the PGI 2013 compiler suite.  To load the OpenACC compiler, use the command:

```bash
module load pgi/2013
```

A very basic OpenACC example code is provided below `stencil.c`:

```bash
#include <stdio.h>
#include <stdlib.h>

int main(){

        int i,j,it;

        // set the size of our test arrays
        int numel = 2000;

        // allocate and initialize test arrays
        float A[numel][numel];
        float Anew[numel][numel];
        for (i = 0; i < numel; i++){
                for ( j = 0; j < numel; j++){
                        A[i][j] = drand48();
                }
        }

        // apply stencil 1000 times
        #pragma acc data copy(A), create(Anew)
        for (it = 0; it < 1000; it++){

                #pragma acc parallel loop
                for (i = 1; i < numel-1; i++){
                        for (j = 1; j < numel-1; j++){

                                Anew[i][j] = 0.25f * (A[i][j-1] + A[i][j+1] + A[i-1][j] + A[i+1][j]);

                        }
                }

                #pragma acc parallel loop
                for (i = 1; i < numel-1; i++){
                        for (j = 1; j < numel-1; j++){

                                A[i][j] = Anew[i][j];

                        }
                }

        }

        // do something with A[][]

        return 0;

}
```

OpenACC code targeted at an Nvidia GPU must be compiled with the PGI compiler using at least the following options:

```bash
pgcc source_code.c -ta=nvidia -acc
```
