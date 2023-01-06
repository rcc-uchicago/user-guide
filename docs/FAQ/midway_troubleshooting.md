# Frequently Asked Questions
<!-- Inspired by:
https://argonne-lcf.github.io/user-guides/polaris/hardware-overview/machine-overview/ -->

This page provides answers to frequently asked questions when using the Midway2 and Midway3.

=== "Midway2"
    <!-- From these links:
    https://rcc.uchicago.edu/resources/ -->

    ??? question "How can I list the software packages available? "
          At the terminal on the login node you can run
          ```
          module list
          ```
          You can list all the versions of a software package, or a software bundle, with `module avail`

    
          ```
          module avail [package-name]
          ```

        For example,
        ```
        module avail cuda
        ```
        or
        ```
        module avail python
        ```
        You can then show the dependencies of a particular module, its location and the environment variables that are set:
        ```
        module show [package-name]
        ```
        You can load the software package into your environment
        ```
        module load [package-name]
        ```
        which essentially updates the environment variables so that you can access the binaries (with the prepended `PATH`)
        or your application can link with the package libraries (with the modified `LD_LIBRARY_PATH`).
    
    ??? question "How can I install new python packges? "
        The recommended practice is to load an existing python module, create your own environment and then install the packge(s)
        into your own environment.
        ```
        module load python/anaconda-2021.05
        ```
        then create and activate your own environment
        ```
        conda create --prefix=/path/to/your/env/my-env python=3.8
        conda activate my-env
        ```
        or with `venv`
        ```
        python -m venv /path/to/your/env/my-env
        source /path/to/your/env/my-env/bin/activate
        ```
        Finally, install your packages via `conda install` or `pip install`:
        ```
        conda install -c conda-forge numpy
        ```
        or
        ```
        pip install numpy
        ```
        Whenever possible, specify the variant of the package that you want explicitly that matches the modules you already loaded.
        ```
        pip install tensorflow cudatoolkit=11.2 cudnn=8.1.0
        ```
        or
        ```
        pip3 install torch==1.12.0+cu113 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
        ```

        Reference: [PyTorch documentation](https://pytorch.org/get-started/locally/)

    
    
    ??? question "How can I use Tensorflow and PyTorch with GPUs? "
          You need to install these packages with the existing CUDA toolkit modules on Midway2 (see `module avail cuda`),
          then load the module via `module load cuda/11.3`. Then install Tensorflow and PyTorch into your own environment (see above).
                
          You can check if the installed version of Tensorflow in your enviroment can access to the GPUs on a GPU compute node via
          ```
          python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
          ```
            Similarly for PyTorch with GPU support
            ```
            python -c "import torch; print(torch.vresion.cuda)"
            ```
            Reference: [Tensorflow documentation](https://www.tensorflow.org/install/pip)
    
    <!-- How can I compile third-party packages or my own codes? -->


=== "Midway3"
    <!-- From these links:
    https://mdw3-docs.rcc.uchicago.edu/ -->

    ??? question "How can I list the software packages available? "
        At the terminal on the login node you can run
        ```
        module list
        ```
        You can list all the versions of a software package, or a software bundle, with `module avail`
        ```
        module avail [package-name]
        ```
        For example,
        ```
        module avail cuda
        ```
        or
        ```
        module avail python
        ```
        You can then show the dependencies of a particular module, its location and the environment variables that are set:
        ```
        module show [package-name]
        ```
        You can load the software package into your environment
        ```
        module load [package-name]
        ```
        which essentially updates the environment variables so that you can access to the binaries (with the prepended `PATH`)
        or your application can link with the package libraries (with the modified `LD_LIBRARY_PATH`).
    ??? question "How can I install new python packges? "
          The recommended practice is to load an existing python module, create your own environment and then install the packge(s)
            into your own environment.
            ```
            module load python/anaconda-2021.05
            ```
            then create and activate your own environment
            ```
            conda create --prefix=/path/to/your/env/my-env python=3.8
            conda activate my-env
            ```
            or with `venv`
            ```
            python -m venv /path/to/your/env/my-env
            source /path/to/your/env/my-env/bin/activate
            ```
            Finally, install your packages via `conda install` or `pip install`:
            ```
            conda install -c conda-forge numpy
            ```
            or
            ```
            pip install numpy
            ```
            Whenever possible, specify the variant of the package that you want explicitly that matches the modules you already loaded.
            ```
            pip install tensorflow cudatoolkit=11.2 cudnn=8.1.0
            ```
            or
            ```
            pip3 install torch==1.12.0+cu113 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
            ```

            Reference: [PyTorch documentation](https://pytorch.org/get-started/locally/)
    <!-- ??? question "How can I compile third-party packages or my own codes? " -->
    ??? question "How can I use Tensorflow and PyTorch with GPUs? "
          You need to install these packages with the existing CUDA toolkit modules on Midway3 (see `module avail cuda`),
          then load the module via `module load cuda/11.3`. Then install Tensorflow and PyTorch into your own environment (see above).
                
          You can check if the installed version of Tensorflow in your enviroment can access to the GPUs on a GPU compute node via
          ```
          python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
          ```
          Similarly for PyTorch with GPU support
            ```
            python -c "import torch; print(torch.vresion.cuda)"
            ```
            Reference: [Tensorflow documentation](https://www.tensorflow.org/install/pip)
           
