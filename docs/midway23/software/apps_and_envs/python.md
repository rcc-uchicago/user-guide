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

**Step 1**: Load the desired Python module. This can be done on a login node, or on a compute node via an interactive job.

**Step 2**: Determine the IP address of the host you are on. Whether you are on a login node or a compute node,
you can use this command to get your IP address:

```
HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
echo $HOST_IP
```
which can be either `128.135.x.y`, or `10.50.x.y`.

**Step 3**: Launch Jupyter with:

=== "Midway2"
    ```
    jupyter-notebook --no-browser --ip=$HOST_IP
    ```
===+ "Midway3"
    ```
    jupyter-notebook --no-browser --ip=$HOST_IP --port=15021
    ```
    ???+ note
        Jupyter on Midway3 typically requires you to specify a port in the range of 15000-30000. You can
        generate a random number in this range:
        ```
        PORT_NUM=$(shuf -i15001-30000 -n1)
        echo $PORT_NUM
        ```

which will give you a URL with a token, for example,

```default
http://10.50.221.192:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```

If there is a problem with the port, your browser will complain. In that case, please try the next available port
with the flag `--port=<port number>`, or use the command `shuf`  above to get a random port number before launching
```
PORT_NUM=$(shuf -i15001-30000 -n1)
jupyter-notebook --no-browser --ip=$HOST_IP --port=$HOST_NUM
```

**Step 4**: Open the returned URL in the browser on your local machine. Note that if you do
not specify `--no-browser --ip=`, the web browser will be launched on the node and
the URL returned cannot be used on your local machine.

As of Feb 2023, this step may hang and you may get the `The site is not reachable` error from the browser.
If this is the case, open another terminal window on your local machine and run

```
ssh -N -f -L 15021:midway3-login3:15021 [your-CNetID]@midway3.rcc.uchicago.edu
```
This command will create an SSH connection from your local machine to `midway3-login3` node and forwards the 15021 port
to your local host at port 15021. Note that the port number should be consistent across all the steps (15021 in this example).
You can find out the meaning for the arguments used in this command at [explainshell.com](https://explainshell.com).

If you are on a compute node, e.g. `midway3-0248`, then replace `midway3-login3` with `midway3-0248` in the above `ssh` command.

After successfully logging with 2FA as usual, you will be able to open the URL in the browser on your local machine.

**Step 5**: To kill Jupyter, go back to the first terminal window where you launch Jupyter Notebook
and press `Ctrl+c` and then confirm with `y` that you want to stop it.


