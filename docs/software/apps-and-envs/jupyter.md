# Notebooks
## Jupyter

Jupyter Notebook is a useful tool for python users because it provides
interactive web-based computing. JupyterLab is the next-generation IDE-like counterpart of Jupyter Notebook with more advanced features for data science, scientific computing, computational journalism, and machine learning. It has a modular structure that allows you to create and execute multiple documents in different tabs in the same window.

For lighweight work, you can launch Jupyter on a login node and then forward its interface to your local machine but have all the computation work done on Midway. Note that resources will be shared will users and no specific hardware will be provided like big RAM or GPUs. If you want to perform heavy compute, you will need to request resources via an interactive or batch job before launching Jupyter notebook.

### Jupyter on Login Nodes
Connect to a Midway login node:

**Step 1**: Load a Python module. 
**Step 2**: Activate a python virtual environment that already has ipykernel package installed. If you haven't created one, follow the stateps from the Python article.
**Step 3**: Set the HOST_IP and PORT_NUM variables. HOST_IP is the IP address of the login node, and PORT_NUM is the arbitrary free port that Jupyter will listen to:

```
HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
PORT_NUM=$(shuf -i15001-30000 -n1)
```
and launch the Notebook server as earlier
```
jupyter-notebook --no-browser --ip=$HOST_IP --port=$PORT_NUM
```
which will give you two URLs with a token, one with the external address `128.135.x.y`, and another with the on-campus address `10.50.x.y`, or with your local host `127.0.0.*`. If you do not specify `--no-browser --ip=`, the web browser will be launched on the node and the URL returned cannot be used on your local machine. The URLs would be something like

```default
http://128.135.167.77:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
http://127.0.0.1:15021/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```

The on-campus address `10.50.x.y` is only valid when you are connecting to Midway2 or Midway3 via VPN. 

**Step 4**: To kill Jupyter, go back to the first terminal window where you launch Jupyter Notebook
and press `Ctrl+c` and then confirm with `y` that you want to stop it.


### Jupyter on Compute Nodes
If you launch Jupyter Notebook on a compute node, the on-campus URL like `10.50.x.y` will be returned instead of `128.135.x.y`.

**Step 1**: Write a script for a jupyter job, `jupyter_on_compute.sh`, replacing [pi-cnetid] with the PI account you want to charge for SUs and adjusting requested resources. Note, that on Midway2, the cluster variable should also be changed to midway2.rcc.uchicago.edu as well as the Python module name can be different. Make sure that the activated environment includes the ipykernel packages and its dependencies. 

```
#!/bin/bash
#SBATCH --job-name=jupy-job
#SBATCH --output=jupy-%J.out
#SBATCH --error=jupy-%J.err
#SBATCH --account=[pi-account]
#SBATCH --time=04:00:00
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=4GB

module load python/miniforge-25.3.0
source activate base

cd $SLURM_SUBMIT_DIR

HOST_IP=`/sbin/ip route get 8.8.8.8 | awk '{print $7;exit}'`
PORT_NUM=$(python3 -c "import socket; s=socket.socket(); s.bind(('', 0)); print(s.getsockname()[1]); s.close()")
NODE=$(hostname -s)
USER=$(whoami)
CLUSTER='midway3.rcc.uchicago.edu'

echo "ssh -N -L $PORT_NUM:$NODE:$PORT_NUM $USER@$CLUSTER"

jupyter lab --no-browser --ip=$HOST_IP --port=$PORT_NUM
```
**Step 2**: Submit the batch job and check that it is running:
```
sbatch jupyter_on_compute.sh
squeue --format="%.18i %.9P %c %.30j %.8u %.8T %.10M %.9l %.6D %R" --me
```
script and the job gets running with a job ID assigned, you can check the output log `output-[jobID].txt` to obtain the URLs.

If you are using on-campus network or VPN, you can copy-paste (or `Ctrl` + click) the URL with the external address, or the URL with the on-campus address into the browser's address bar. 

Without VPN, you need to use SSH tunneling to connect to the Jupyter server launched on the Midway2 (or Midway3) login.

**Step 3**: Set up a tunnel to the Jupyter running on the compute node. Open jupy-[JobID].out and copy a command to forward port from a compute node to your local machine. Open your local terminal (powershell, mobaxterm, terminus, etc) and run this command, which will look like this with different variables assigned by the job:
```
ssh -N -L 52915:midway3-0008:52915 cnetid@midway3.rcc.uchicago.edu
```
It will prompt for 2FA and once successful, start a foreground process enabling the tunnel. Don't close the terminal since the tunnel must remain open while you work with Jupyter. The port number should be consistent across all the steps. 

**Step 4**: Connect to the Jupyter server. Open jupy-[JobID].err and click the URL starting with `http://127.0.0.1:15021/?token=....`. It will open a local browser and connect to the Jupyter server. Note, that if you open this file in VScode and you have an automated port forwarding enabled, then clicking the link will not work because VScode will attempt to forward the port from the login node instead of the compute node where the Jupyter is running. Either disable the autoforwarding in VScode or copy and paste the URL in your address bar instead to clicking on it.

**Step 5**: To kill Jupyter, run `scancel [JobID]`. Closing your terminal with foreqround process will only interrupt connection but the Jupyter server will remain running on the compute node if the job is not terminated.