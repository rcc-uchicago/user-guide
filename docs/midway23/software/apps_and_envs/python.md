# Python and Anaconda

## Getting Started

Different versions of Python on Midway are offered as modules. To check the full list of Python modules
use the `module avail python` command.

The command `module load python` will load the default module: an Anaconda distribution
of Python. Note that there are multiple different Anaconda distributions available.  

Once you load an Anaconda distribution, you can list all available public environments with:
```
conda env list  
```
To activate an environment, run:
```
source activate <ENV NAME>
```
where `<ENV NAME>` is the name of the environment for a public environment,
or the full path to the environment, if you are using a personal one. You can deactivate an environment
with:
 ```
 conda deactivate
 ```

!!! danger

    Never run `conda init`! Use `source activate` instead of `conda activate`**.**
    `conda init` has been known to break ThinLinc.

## Managing Environments

With each Anaconda distribution, we have a small selection of widely used environments. Many, such as
Tensorflow or DeepLabCut should be loaded through their modules (i.e., `module load tensorflow`), which automate the loading of other
relevant libraries that are available as modules.

If you need packages not available in the global environment, you can make a personal environment for
them. If you want to copy an existing environment to modify it, you can do that with:
```
conda create --prefix=/path/to/new/environment --clone <EXISTING ENVIRONMENT>
``` 
If you want to make a clean environment, you can do that with
```
conda create --prefix=/path/to/new/environment python=<PYTHON VERSION NUMBER>
```

Once your environment is set up how you want, especially if it is in your scratch space, you may want
to create a backup of the environment into a YAML file. You do that after activating the environment
with `conda env export > environment.yml`. That YAML file can then be used to recreate the environment
with `conda env create --prefix=/path/to/new/environment -f environment.yml`.

!!! note
    Anaconda may sometimes cause issues with ThinLinc. If you are experiencing frequent, spontaneous disconnections from ThinLinc, remove any sections involving "conda" or "anaconda" from the file `~/.bshrc` (in your home directory).
    
## Managing Packages

In the Anaconda distributions of Python, you should generally be using a personal environment to manage
packages. Once you activate your environment, you can install packages with `conda install` or
`pip install`. As per the advice of the Anaconda software authors, any  `pip install` packages
should be installed after `conda install` packages.


## Using Python

On Midway, python can be launched, after loading a desired module, at the terminal with the command:

```default
python
```

To leave the launched interactive shell, use:

```default
exit()
```

If you already have a python script, use this command to run it:

```default
python your_script.py
```

### Python Interactive Plotting

For interactive plotting, it is necessary to set the matplotlib backend to a
graphical backend. Here is an example:

```python
#!/usr/bin/env python

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

If you are saving files and viewing them with the *display* command, you may
experience rapid flickering. There seems to be an issue with image
transparency, use a command like this to disable the transparency:

```default
display -alpha off <image>
```

## Running Jupyter Notebooks

Jupyter notebook is a useful tool for python users because it provides
interactive computing. You can launch Jupyter on Midway, open it in the
browser on your local machine and have all the computation work done
on Midway. If you want to perform heavy compute, you will need to start an interactive session (please see
[Running Jobs](/midway23/midway_submitting_jobs) on how to get an interactive session)
before launching Jupyter notebook otherwise you may use one of the login nodes.

The steps to launch Jupyter are as follows:

Step 1: Load the desired Python module

Step 2: Determine your ip address. Whether you are on a login node or a compute node,
you can use this command to get your ip address:

```
/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'
```

Step 3: Launch Jupyter with:

=== "Midway2"
    ```
    jupyter-notebook --no-browser --ip=<ip address>
    ```
===+ "Midway3"
    ```
    jupyter-notebook --no-browser --ip=<ip address> --port=15000
    ```
    ???+ note
        Jupyter on Midway3 typically requires you to specify a port in the range of 15000-30000

which will give you a URL with a token. For example:

```default
http://10.50.221.192:8888/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```

If there is a problem with the port, your browser will complain. In that case, please try the next available port
with the flag `--port=<port number>`

Step 4: Open the returned URL in the browser on your local machine. Note that if you do
not specify `--no-browser --ip=`, the web browser will be launched on the node and
the URL returned cannot be used on your local machine.

Step 5: To kill Jupyter, press `Ctrl+c` and then confirm with `y` that you want to
stop it
