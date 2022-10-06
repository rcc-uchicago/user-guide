# Interactive Jobs

After submitting an “interactive job” on Midway, the Slurm job scheduler will connect you to a compute node, and will load up an interactive shell environment for you to use on that compute node. This interactive session will persist until you disconnect from the compute node, or until you reach the maximum requested time. The default requested time is 2 hours.

## sinteractive
The command `sinteractive` is the recommended Slurm command for requesting an interactive session. As soon as the requested resources become available, sinteractive will do the following:

1. Log in to the node.

2. Change into the directory you were working in.

3. Set up X11 forwarding for displaying graphics.

4. Transfer your current shell environment, including any modules you have previously loaded.

To get started (with the default interactive settings), simply enter `sinteractive` in the command line:

```
$ sinteractive
```

By default, an interactive session times out after 2 hours. If you would like more than 2 hours, be sure to include a `--time=HH:MM:SS` flag to specify the necessary amount of time. For example, to request an interactive session for 6 hours, run the following command:

```
$ sinteractive --time=06:00:00
```

There are many additional options for the `sinteractive` command, including options to select the number of nodes, the number of cores per node, the amount of memory, and so on. For example, to request exclusive use of two compute nodes on the Midway **broadwl** partition for 8 hours, enter the following:

```
$ sinteractive --exclusive --partition=broadwl --nodes=2 --time=08:00:00
```

For more details about these and other useful options, read below about the `sbatch` command, and see [Running jobs on midway](../running-jobs/index.md#running-jobs). Note that all options available in the `sbatch` command are also available for the `sinteractive` command.

There is a `debug` QoS setup on the `broadwl` partition to help users quickly access some resources to debug or test their code before submitting their jobs to the main `broadwl` partition. The `debug` QoS will allow you to run one job and get up to 4 cores for 15 minutes. To use the `debug` QoS, you have to specify `--time` which should be 15 minutes or less. For example, to get 2 cores for 15 minutes, you could run:

```
$ sinteractive --qos=debug --time=00:15:00 --ntasks=2
```

##srun
An alternative to the `sinteractive` command is the `srun` command:

```
$ srun --pty bash
```

Unlike `sinteractive`, this command does not set up X11 forwarding, which means you cannot display graphics using `srun`. Both the `srun` and `sinteractive` commands have the same command options.