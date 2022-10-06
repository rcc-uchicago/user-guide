# Running Jupyter Notebooks

The Jupyter notebook is a useful tool for python users because it provides
interactive computing. You can launch Jupyter on Midway, open it in the
browser on your local machine and have all the computation work done
on Midway. If you want to perform heavy compute, you will need to start an interactive session (please see
[Interactive Jobs](../../../using-midway/index.md#interactive-jobs) on how to get an interactive session)
before launching Jupyter notebook otherwise you may use one of the login nodes.

**NOTE**: Compute nodes are only visible on internal UChicago network. If
you want to launch Jupyter on a compute node (using an interactive session), you will need to either
be on campus or use VPN. However, you may launch it on a login node anytime.

The steps to launch Jupyter are as follows:


1. Load the desired Python module

2. Determine your ip address. Whether you are on a login node or a compute node,
you can use this command to get your ip address:

```default
/sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}'
```


1. Launch Jupyter with:

> jupyter-notebook –no-browser –ip=<ip address>

or in Python 3.x with:

```default
jupyter-notebook --no-browser --ip=<ip address>
```

which will give you a URL with a token. For example:

```default
http://10.50.221.192:8888/?token=9c9b7fb3885a5b6896c959c8a945773b8860c6e2e0bad629
```

By default, the above command listens on port 8888. If the port is already taken
by another user, it will complain. In that case, please try the next available port
with the option:

```default
--port=<port number>
```

4. Open the returned URL in the browser on your local machine. Note that if you do
not specify `--no-browser --ip=`, the web browser will be launched on the node and
the URL returned cannot be used on your local machine.

5. To kill Jupyter, press `Ctrl+c` and then confirm with `y` that you want to
stop it
