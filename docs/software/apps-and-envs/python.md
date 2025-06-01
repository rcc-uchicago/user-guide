

# 1. Introduction

Welcome! This guide provides best practices and recommendations for using Python on the Midway2 and Midway3 clusters at UChicago RCC. It covers Python distribution choices, environment management, interactive computing, and troubleshooting tips for research computing. 

- **Audience:** Researchers, students, and staff using Python on Midway clusters.
- **Scope:** Standard Python modules, Miniforge, uv, Mamba, Jupyter, plotting, and more.
- **Tip:** For best results, read through the recommendations and best practices before starting a new project.

[//]: # (TOC placeholder for MkDocs Material)
[[toc]]

---

# 2. Recommendations

## 2.1. Python distribution recommendations

Choosing the right Python distribution is essential for reproducibility, ease of use, and compatibility with Midway resources. The table below summarizes the main options and when to use each.

| Distribution                | Module Name/Version                 | Best for                        | Notes                                         |
|-----------------------------|-------------------------------------|----------------------------------|-----------------------------------------------|
| Standard Python (recommended) | `python/3.11.9`, `python/3.8.0`, `python/2.7` (Midway3)<br>`python/3.9.18` (Midway2) | Most research, production, reproducibility | Minimal, clean installs. Use for scripts, pipelines, and most research. |
| Miniforge (conda/mamba)     | `python/miniforge-24.1.2`, `python/miniforge-25.3.0` | Scientific computing, data science | Flexible, includes mamba for fast env/package management. |
| Anaconda                    | Not recommended                     | Legacy only                     | License restrictions, excessive inode usage, large storage footprint. |

!!! tip "Quick advice:"
    - **Use Standard Python** for most research, scripting, and production workflows. It ensures a clean, reproducible environment.
    - **Use Miniforge** if you need many scientific/data science packages or want to manage environments with conda/mamba.
    - **Avoid Anaconda** on Midway; it has commercial license restrictions and causes excessive inode consumption in home directories.

!!! warning "Important: Anaconda Licensing and Inode Usage Issues"
    **Anaconda has implemented commercial license restrictions** for organizations with over 200 employees, affecting many academic institutions. Additionally, a full Anaconda installation can exceed 3GB in size and create over 100,000 small files, which quickly exhausts inode quotas. On Midway clusters, home directories typically have strict inode quotas (around 30,000), and a single Anaconda installation can consume most or all of this quota, preventing you from creating additional files.

**To see available versions:**
```bash
module avail python
```

**To load a module:**
```bash
module load python/3.11.9       # Standard Python (recommended)
module load python/miniforge-25.3.0  # Miniforge (conda/mamba)
```

- For most users, start with Standard Python. If you need conda-style environments or many scientific packages, switch to Miniforge.
- Both Standard Python and Miniforge are fully supported and optimized for Midway clusters.

- On Midway2, available versions:
  - `python/miniforge-25.3.0`
  - Recommended conda distribution for research
  - Uses conda-forge channel by default
    - **conda-forge** is a community-driven collection of conda packages that provides up-to-date, well-maintained, and widely used scientific software. It is the recommended source for most research software packages, ensuring compatibility and reliability.
  - Smaller footprint than Anaconda
  - Includes Mamba for faster package resolution

!!! note "Why Miniforge over Anaconda?"
    Miniforge is strongly preferred over Anaconda for research computing on Midway clusters for several reasons:
    - **No license restrictions for any use**, unlike Anaconda's commercial restrictions
    - **Significantly fewer files and inodes** - Anaconda installations can exceed 3GB and create over 100,000 small files
    - **Smaller disk footprint** - Requires less storage space in your quota
    - **Faster package installation** with Mamba support
    - **Uses conda-forge by default** for more up-to-date scientific packages
    - **Better performance on HPC environments** with lower overhead

!!! warning "Managing Inode Usage with Conda Environments"
    If you use any conda-based distribution (Miniforge, Anaconda, etc.):
    
    1. Install environments in `/scratch/midway3/$USER/conda_envs` rather than your home directory
    2. Run `conda clean --all` regularly to remove unused package caches
    3. Limit the number of environments you create and maintain
    4. Use `df -i` to check your current inode usage
    5. Consider Python virtual environments (venv) for smaller projects

- For most users, start with Standard Python. If you need conda-style environments or many scientific packages, switch to Miniforge.
- Both Standard Python and Miniforge are fully supported and optimized for Midway clusters.

   - On Midway2, available versions:
     - `python/miniforge-25.3.0`
   - Recommended conda distribution for research
   - Uses conda-forge channel by default
     - **conda-forge** is a community-driven collection of conda packages that provides up-to-date, well-maintained, and widely used scientific software. It is the recommended source for most research software packages, ensuring compatibility and reliability.
   - Smaller footprint than Anaconda
   - Includes Mamba for faster package resolution

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

---

# 3. Best Practices

## 3.1. Environment management

Once you load a Python distribution, you can list all available public environments with:
```bash
conda env list  
```

To activate an environment, run:
```bash
source activate <ENV_NAME>
```

!!! info "Terminology: env"
    In this guide, 'env' is shorthand for 'environment'—a self-contained directory with its own Python and packages.

!!! tip "Why use `source activate` instead of `conda activate` (or `mamba activate`)?"
    While **`conda activate`** is the modern command for activating environments, it may not function reliably in ThinLinc or certain non-interactive shell environments on Midway3. This is because **`conda activate`** (and **`mamba activate`**) requires the shell to be properly initialized through **`conda init`**, which can lead to issues or disrupt ThinLinc sessions. By using **`source activate`**, you can bypass these complications and ensure a smooth environment activation process. This approach is intentional and recommended for maintaining compatibility with ThinLinc and RCC clusters, where stability is crucial for user sessions.

!!! danger "Do not run `conda init`"
    Never run `conda init`! Use `source activate` instead of `conda activate`.
    `conda init` has been known to break ThinLinc.

### Environment best practices

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

### Default domain-specific environments

The `python/miniforge-25.3.0` module comes with several pre-configured domain-specific environments. Each environment is optimized for a specific research domain. Here’s a quick comparison:

| Environment | Activation command      | Best for                        | Core packages / Tools                           |
|-------------|------------------------|----------------------------------|-------------------------------------------------|
| sci         | `source activate sci`  | Scientific computing, data analysis | numpy, scipy, pandas, matplotlib, seaborn, scikit-learn, JupyterLab, ipython, h5py, psutil |
| ml          | `source activate ml`   | Deep learning, ML research       | tensorflow, pytorch, scikit-learn, keras, xgboost, lightgbm, matplotlib, seaborn           |
| bio         | `source activate bio`  | Genomics, bioinformatics         | biopython, samtools, bcftools, bedtools, fastqc, cutadapt, multiqc, pandas, scikit-bio     |
| geo         | `source activate geo`  | GIS, earth science               | gdal, rasterio, geopandas, cartopy, xarray, netcdf4, matplotlib, pyproj                    |
| hpc         | `source activate hpc`  | Parallel/distributed computing   | mpi4py, dask, dask-jobqueue, joblib, ipyparallel, numpy, pandas                            |

All environments include:
- Python 3.11
- Mamba for fast package management
- Pip for additional package installation
- Common development tools

!!! tip "Choosing your environment"
    Select the environment that matches your research domain to get started quickly. You can always install extra packages or create a custom environment based on these templates.



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

!!! tip "Quick Overview: Interactive Plotting"
    For interactive plotting on Midway, you need to set the matplotlib backend to a graphical backend (like Qt4Agg). This enables plots to display correctly when using remote sessions or ThinLinc.

??? note "Click to know more: Plotting Example and Troubleshooting"
    Here is an example of setting up matplotlib for interactive plotting:

    ```python
    #!/usr/bin/env python
    import matplotlib
    matplotlib.use('Qt4Agg')
    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()
    ```

    If you are saving files and viewing them with the *display* command, you may experience rapid flickering. There seems to be an issue with image transparency—use a command like this to disable the transparency:

    ```bash
    display -alpha off <image>
    ```

---

# 4. Additional Tips

## 4.1. Python Interactive Plotting

!!! tip "Quick Overview: Interactive Plotting"
    For interactive plotting on Midway, you need to set the matplotlib backend to a graphical backend (like Qt4Agg). This enables plots to display correctly when using remote sessions or ThinLinc.

??? note "Click to know more: Plotting Example and Troubleshooting"
    Here is an example of setting up matplotlib for interactive plotting:

    ```python
    #!/usr/bin/env python
    import matplotlib
    matplotlib.use('Qt4Agg')
    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()
    ```

    If you are saving files and viewing them with the *display* command, you may experience rapid flickering. There seems to be an issue with image transparency—use a command like this to disable the transparency:

    ```bash
    display -alpha off <image>
    ```

## 4.2. Jupyter Notebooks and JupyterLab

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

---

# Python Documentation Migration

The Python documentation has moved! Please see the new, expanded documentation at:

- [Python Overview](./python/index.md)
- [Python Environments](./python/environments.md)
- [Troubleshooting & Known Issues](./python/troubleshooting.md)

These pages provide up-to-date guidance, best practices, and troubleshooting tips for Python usage on RCC Midway clusters.

---

_Last updated: May 30, 2025_
