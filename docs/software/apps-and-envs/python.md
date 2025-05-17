# Python on Midway2 and Midway3

## Getting Started

Different versions of Python are available as modules on both Midway2 and Midway3. To see available versions:
```bash
module avail python
```
### Python Distribution Recommendations

For research computing on Midway clusters, we recommend:

1. **For Standard Python**: Use version-specific modules
   - On Midway3: (e.g., `python/3.11.9`)
   - On Midway2: (e.g., `python/3.9.18`)
   - Clean, minimal installation
   - Best for reproducible research
   - Ideal for production environments

2. **For Scientific Computing**: Use Miniforge (e.g., `python/miniforge-25.3.0`)
   - Recommended conda distribution for research
   - Uses conda-forge channel by default
   - Smaller footprint than Anaconda
   - Includes mamba for faster package resolution
   - Available on both Midway2 and Midway3

!!! note "Why Miniforge over Anaconda?"
    While Anaconda is excellent for teaching and exploration, Miniforge is preferred for research computing because:
    - Smaller initial footprint
    - Faster installation and updates
    - Uses conda-forge by default
    - Better suited for HPC environments
    - No license restrictions for commercial use

## Managing Storage and Cache

### Conda/Mamba Cache Management

By default, conda/mamba stores package cache in your home directory, which can quickly fill up. To manage this:

1. **Use Temporary Cache (Recommended)**:
```bash
# Before loading Python module
export USE_CONDA_CACHE=0  # Default behavior
module load python/miniforge-25.3.0
```

2. **Use Persistent Cache (Optional)**:
```bash
# Only if you need to keep downloaded packages
export USE_CONDA_CACHE=1
module load python/miniforge-25.3.0
```

### UV Package Manager

uv is a modern, fast alternative to pip for package management (available on both Midway2 and Midway3):

```bash
# Load modules
module load python/miniforge-25.3.0  # or other Python version
module load uv

# Create virtual environment (faster than venv)
uv venv myenv

# Activate
source myenv/bin/activate

# Install packages (much faster than pip)
uv pip install numpy pandas
```

!!! note "UV Cache Behavior"
    By default, uv uses a temporary cache. To enable persistent cache:
    ```bash
    export USE_UV_CACHE=1
    module load uv
    ```

## Environment Management

### Managing Environments

Once you load a Python distribution, you can list all available public environments with:
```bash
conda env list  
```

To activate an environment, run:
```bash
source activate <ENV NAME>
```
where `<ENV NAME>` is the name of the environment for a public environment,
or the full path to the environment, if you are using a personal one. You can deactivate an environment
with:
```bash
conda deactivate
```

!!! danger
    Never run `conda init`! Use `source activate` instead of `conda activate`.
    `conda init` has been known to break ThinLinc.

### Environment Best Practices

#### 1. Environment Location

=== "Midway2"
    Store environments in project space, not home directory:
    ```bash
    # Create environment in project space
    conda create --prefix=/project2/PI_NAME/USER/envs/myenv python=3.11

    # Or with uv (recommended for faster creation)
    module load uv
    cd /project2/PI_NAME/USER/envs
    uv venv myenv
    ```

=== "Midway3"
    Store environments in project space, not home directory:
    ```bash
    # Create environment in project space
    conda create --prefix=/project/PI_NAME/USER/envs/myenv python=3.11

    # Or with uv (recommended for faster creation)
    module load uv
    cd /project/PI_NAME/USER/envs
    uv venv myenv
    ```

#### 2. Environment Activation

For conda environments:
=== "Midway2"
    ```bash
    # Direct activation (long path)
    source activate /project2/PI_NAME/USER/envs/myenv

    # Or create symlink for convenience
    ln -s /project2/PI_NAME/USER/envs/myenv ~/.conda/envs/myenv
    source activate myenv
    ```

=== "Midway3"
    ```bash
    # Direct activation (long path)
    source activate /project/PI_NAME/USER/envs/myenv

    # Or create symlink for convenience
    ln -s /project/PI_NAME/USER/envs/myenv ~/.conda/envs/myenv
    source activate myenv
    ```

For uv environments:
=== "Midway2"
    ```bash
    source /project2/PI_NAME/USER/envs/myenv/bin/activate
    ```

=== "Midway3"
    ```bash
    source /project/PI_NAME/USER/envs/myenv/bin/activate
    ```

#### 3. Environment Documentation

Always document your environment:

```bash
# For conda environments
conda env export --from-history > environment.yml

# For uv environments
uv pip freeze > requirements.txt
```

#### 4. Storage Management Tips

1. **Clean Unused Packages**:
```bash
mamba clean --all  # Remove unused package cache
# or
conda clean --all  
```

2. **Use Project Space**:
=== "Midway2"
    ```bash
    # Set default env location
    export CONDA_ENVS_PATH=/project2/PI_NAME/USER/envs
    ```

=== "Midway3"
    ```bash
    # Set default env location
    export CONDA_ENVS_PATH=/project/PI_NAME/USER/envs
    ```

3. **Minimize Environment Size**:
```bash
# Only specify needed packages
mamba create -n myenv python=3.11 numpy pandas
```

4. **Share Common Environments**:
=== "Midway2"
    ```bash
    # Create read-only group environment
    conda create --prefix=/project2/PI_NAME/shared_envs/analysis python=3.11
    chmod -R a-w /project2/PI_NAME/shared_envs/analysis
    ```

=== "Midway3"
    ```bash
    # Create read-only group environment
    conda create --prefix=/project/PI_NAME/shared_envs/analysis python=3.11
    chmod -R a-w /project/PI_NAME/shared_envs/analysis
    ```

### Cloning and Backing Up Environments

If you want to copy an existing environment to modify it:
```bash
conda create --prefix=/path/to/new/environment --clone <EXISTING ENVIRONMENT>
```

To backup an environment to a YAML file:
```bash
conda env export > environment.yml
```

To recreate from a YAML file:
```bash
conda env create --prefix=/path/to/new/environment -f environment.yml
```

!!! note
    Anaconda may sometimes cause issues with ThinLinc. If you are experiencing frequent, spontaneous disconnections from ThinLinc, remove any sections involving "conda" or "anaconda" from the file `~/.bashrc` (in your home directory).

### Default Domain-Specific Environments

The `python/miniforge-25.3.0` module comes with several pre-configured domain-specific environments that you can use directly. Each environment is optimized for specific research domains:

1. **Scientific Computing Environment (`sci`)**:
   ```bash
   source activate sci
   ```
   - Core packages: numpy, scipy, pandas, matplotlib, seaborn, scikit-learn
   - Includes: JupyterLab, ipython, h5py, psutil
   - Best for: General scientific computing and data analysis

2. **Machine Learning Environment (`ml`)**:
   ```bash
   source activate ml
   ```
   - Core packages: tensorflow, pytorch, scikit-learn
   - Additional tools: keras, xgboost, lightgbm
   - Visualization: matplotlib, seaborn
   - Best for: Deep learning and machine learning research

3. **Bioinformatics Environment (`bio`)**:
   ```bash
   source activate bio
   ```
   - Bioinformatics tools: biopython, samtools, bcftools, bedtools
   - Quality control: fastqc, cutadapt, multiqc
   - Analysis: pandas, numpy, matplotlib, scikit-bio
   - Best for: Genomics and bioinformatics workflows

4. **Geospatial Environment (`geo`)**:
   ```bash
   source activate geo
   ```
   - GIS tools: gdal, rasterio, geopandas
   - Analysis: cartopy, xarray, netcdf4
   - Visualization: matplotlib, pyproj
   - Best for: Geographic information systems and Earth science

5. **High-Performance Computing Environment (`hpc`)**:
   ```bash
   source activate hpc
   ```
   - Parallel computing: mpi4py, dask, dask-jobqueue
   - Task management: joblib, ipyparallel
   - Core tools: numpy, pandas
   - Best for: Parallel and distributed computing

Each environment includes:
- Python 3.11
- Mamba for fast package management
- Pip for additional package installation
- Common development tools

!!! tip "Environment Selection"
    Choose the environment that best matches your research domain to get started quickly. You can always install additional packages or create a custom environment based on these templates.


## Using Python

On Midway, `python` can be launched, after loading a desired module, at the terminal with the command:

```default
python
```

To leave the launched interactive shell, use:

```default
exit()
```
or
```default
quit()
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

Jupyter Notebook is a useful tool for python users because it provides
interactive web-based computing. You can launch Jupyter Notebooks on Midway, open it in the
browser on your local machine and have all the computation work done
on Midway. If you want to perform heavy compute, you will need to start an [interactive session](../../slurm/sinteractive.md) before launching Jupyter notebook, otherwise you may use one of the login nodes.

The steps to launch Jupyter are as follows:

**Step 1**: Load the desired Python module. This can be done on a login node, or on a compute node via an interactive job or a batch job.

**Step 2**: Determine the IP address of the host you are on. Whether you are on a login node or a compute node,
you can use this command to get your IP address:

```
HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
echo $HOST_IP
```
which can be either `128.135.x.y` (an external address), or `10.50.x.y` (on-campus address).

**Step 3**: Launch Jupyter with:

=== "Midway2"
    ```
    jupyter-notebook --no-browser --ip=$HOST_IP
    ```
    or
    ```
    jupyter-lab --no-browser --ip=$HOST_IP
    ```
===+ "Midway3"
    ```
    jupyter-notebook --no-browser --ip=$HOST_IP --port=15021
    ```
    or
    ```
    jupyter-lab --no-browser --ip=$HOST_IP --port=15021
    ```

where 15021 is an arbitrary port number rather than 8888. If there is a problem with the port already in use, your browser will complain. In that case, please try the another port with the flag `--port=<port number>`, or use the command `shuf`  to get a random number for the port:
```
PORT_NUM=$(shuf -i15001-30000 -n1)
```
and launch the Notebook server as earlier
```
jupyter-notebook --no-browser --ip=$HOST_IP --port=$PORT_NUM
```

which will give you two URLs with a token, one with the external address `128.135.x.y`, and another with the on-campus address `10.50.x.y`, or  with your local host `127.0.0.*`.  The on-campus address `10.50.x.y` is only valid when you are connecting to Midway2 or Midway3 via VPN. The URLs would be something like

```default
http://128.135.167.77:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```
or
```default
http://10.50.260.16:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```
or
```default
http://127.0.0.1:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```

If you launch Jupyter Notebook on a compute node, the URLs with `10.50.x.y` and `127.0.0.1` are likely to be returned.

If you do not specify `--no-browser --ip=`, the web browser will be launched on the node and the URL returned cannot be used on your local machine.

Steps 1 through 3 can be done with a batch job as well. An example job script for launching Jupyter Notebook is given as below.

```
!/bin/bash
#SBATCH --job-name=jupyter-launch
#SBATCH --account=pi-[cnetid]
#SBATCH --output=output-%J.txt
#SBATCH --error=error-%J.txt
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --memb=8GB

module load python/anaconda-2021.05

cd $SLURM_SUBMIT_DIR

HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
PORT_NUM=$(shuf -i15001-30000 -n1)
jupyter-notebook --no-browser --ip=$HOST_IP --port=$PORT_NUM
```

After submitting the job script and the job gets running with a job ID assigned, you can check the output log `output-[jobID].txt` to obtain the URLs.

**Step 4**: Open a web browser on your local machine with the returned URLs.

If you are using on-campus network or VPN, you can use copy and paste (or `Ctrl` + mouse click on) the URL with the external address, or the URL with the on-campus address into the address bar.

Without VPN, you need to use SSH tunneling to connect to the Jupyter server launched on the Midway2 (or Midway3) login or compute nodes in Step 3 from your local machine. To do that, open another terminal window on your local machine and run

```
ssh -N -f -L 15021:<HOST_IP>:15021 <your-CNetID>@midway3.rcc.uchicago.edu
```
where `HOST_IP` is the external IP address of the login node obtained from Step 2, and 15021 is the port number used in Step 3.

This command will create an SSH connection from your local machine to Midway login or compute nodes and forward the 15021 port to your local host at port 15021. The port number should be consistent across all the steps (15021 in this example). You can find out the meaning for the arguments used in this command at [explainshell.com](https://explainshell.com){:target='_blank'}.

After successfully logging with 2FA as usual, you will be able to open the URL `http://127.0.0.1:15021/?token=....`, or equivalently, `localhost:15021/?token=....` in the browser on your local machine.

**Step 5**: To kill Jupyter, go back to the first terminal window where you launch Jupyter Notebook
and press `Ctrl+c` and then confirm with `y` that you want to stop it.


## Running JupyterLab

JupyterLab is the next-generation IDE-like counterpart of Jupyter Notebook with more advanced features for data science, scientific computing, computational journalism, and machine learning. It has a modular structure that allows you to create and execute multiple documents in different tabs in the same window.

## Advanced Tips

### Using Mamba

Mamba is a faster alternative to conda:
```bash
# Instead of conda install
mamba install numpy pandas

# Instead of conda create
mamba create -n myenv python=3.11
```

### Environment Isolation

Keep environments minimal and specific:
```bash
# Create purpose-specific environments
mamba create -n ml-env python=3.11 tensorflow pytorch
mamba create -n geo-env python=3.11 gdal rasterio
```

### Package Installation Order

1. Install conda/mamba packages first
2. Then install pip packages
3. Use uv for faster pip installations

```bash
# Example workflow
mamba install numpy pandas

# Then use uv for pip packages
uv pip install specialized-package
```

!!! warning "Storage Usage"
    - Monitor your environment sizes: `du -sh /path/to/env`
    - Use `mamba clean` or `conda clean` regularly
    - Consider temporary cache for short-term work
    - Archive unused environments to tar files 