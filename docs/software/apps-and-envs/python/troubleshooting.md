# Troubleshooting & Known Issues

This page covers common issues encountered with Python on RCC Midway clusters, including inode/file count problems, Jupyter integration, plotting, and environment conflicts.

## Inode/File Count Issues with Anaconda
- **Problem:** Anaconda environments can create a huge number of files (inodes), quickly exhausting user quotas on HPC systems.
- **Advice:** Prefer Miniforge or Mamba. If you must use Anaconda, regularly check your inode usage and clean up unused environments.
- **Reference:**
  - [UArizona HPC: Anaconda Issues](https://hpcdocs.hpc.arizona.edu/software/popular_software/anaconda/){:target='_blank'}

## Interactive Plotting Issues

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

## Connecting to Jupyter

Jupyter Notebook is a core tool for interactive, web-based Python computing on Midway. You can launch Jupyter Notebooks on Midway, access them in your local browser, and have all computation performed on the cluster. For heavy compute, start an [interactive session](../../slurm/sinteractive.md) before launching Jupyter; otherwise, use a login node.

### Launching Jupyter

**Step 1:** Load the desired Python module (on a login or compute node, via interactive or batch job).

**Step 2:** Determine the IP address of your host:
```bash
HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
echo $HOST_IP
```

**Step 3:** Launch Jupyter:

=== "Midway2"
    ```bash
    jupyter-notebook --no-browser --ip=$HOST_IP
    # or
    jupyter-lab --no-browser --ip=$HOST_IP
    ```
=== "Midway3"
    ```bash
    jupyter-notebook --no-browser --ip=$HOST_IP --port=15021
    # or
    jupyter-lab --no-browser --ip=$HOST_IP --port=15021
    ```

If the port is already in use, try another port with `--port=<port number>`, or use:
```bash
PORT_NUM=$(shuf -i15001-30000 -n1)
jupyter-notebook --no-browser --ip=$HOST_IP --port=$PORT_NUM
```

You will receive URLs with a token, such as:
```
http://128.135.x.y:15021/?token=...
http://10.50.x.y:15021/?token=...
http://127.0.0.1:15021/?token=...
```

If you launch Jupyter on a compute node, the URLs with `10.50.x.y` and `127.0.0.1` are likely to be returned.

If you do not specify `--no-browser --ip=`, the web browser will be launched on the node and the URL returned cannot be used on your local machine.

### Launching via Batch Job

Example job script for launching Jupyter Notebook:
```bash
#!/bin/bash
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

After submitting the job, check the output log for URLs.

### Connecting from Your Local Machine

- If using VPN or on-campus: Open the returned URL in your browser.
- Without VPN: Use SSH tunneling to connect to the Jupyter server:

```bash
ssh -N -f -L 15021:<HOST_IP>:15021 <your-CNetID>@midway3.rcc.uchicago.edu
```

After logging in with 2FA, open `http://127.0.0.1:15021/?token=...` in your browser.

**To kill Jupyter:** Go back to the terminal where you launched Jupyter and press `Ctrl+c`, then confirm with `y`.

## PATH and Environment Conflicts
- **Problem:** Anaconda modifies `.bashrc` and can interfere with other software.
- **Solution:** Disable auto-activation (`conda config --set auto_activate_base false`) or remove Anaconda from your environment. See UArizona's troubleshooting tips.

---

_Last updated: May 30, 2025_
