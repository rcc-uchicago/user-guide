# CUDA-Q

[CUDA-Q](https://nvidia.github.io/cuda-quantum/latest/index.html) is a software package for quantum computing from NVIDIA. Related tutorials can also be found at [CUDA-Q Academic](https://github.com/NVIDIA/cuda-q-academic). CUDA-Q is made available in `midway3` as a singularity file (which has both the C++ version and the Python version) and also as a seperate Python environment via the software module `cudaq` . As with other softwares, please use the compute nodes via interactive sessions or sbatch jobs when using cudaq for computations in `midway` systems. The path to the singularity file and the Python environment could be obtained from the module details via the following command.

```default
module show cudaq
```
The Python environment is available at `CUDAQ_ENV` and the singularity file at `CUDAQ_SIF`. The Python environment could be activated using `source $CUDAQ_ENV` after loading the module `module load cudaq/`. For instructions on using singularity in midway, please refer to [this page](https://docs.rcc.uchicago.edu/software/apps-and-envs/singularity/). 

To use the singularity file for CUDA-Q, please load the singularity module, using `module load singularity/`. And then to use cudaq, we could either use the singularity shell or execute the program directly. For the first approach, please launch the singularity shell using`singularity shell $CUDAQ_SIF`, and then run the Python program e.g. using `python example_program.py` or the C++ program by compiling the code first, e.g. using `nvq++ example_program.cpp -o example.out`, followed by the execution e.g., using `./example.out`.  For the second approach, we could execute Python or C++ program using the `exec` command, e.g. using `singularity exec $CUDAQ_SIF python example_program.py > example_output.txt`, for the case of Python.

When using the NVIDIA GPU resources, please use the `--nv` option with the singularity file e.g, when launching the singularity shell, use `singularity shell --nv $CUDAQ_SIF`.