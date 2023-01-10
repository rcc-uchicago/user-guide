## Managing Jobs
The Slurm job scheduler provides several command-line tools for checking on the status of your jobs and for managing them.

### Checking Job Status
Use the `squeue` (slurm queue) command to check on the status of jobs. Running `squeue` with no flags will show the full queue (all pending and running jobs.)


 
To view only the jobs that you have submitted, use the ```--user``` flag.
```
squeue --user=<CNetID>
```
???+ note
    Any job with 0:00 in the TIME column is still waiting in the queue.

To get information about all jobs that are waiting to run on the `gpu` partition, enter:
```
squeue --state=PENDING --partition=gpu
```

To get information about all your jobs that are running on the `gpu` partition, type:
```
squeue --state=RUNNING --partition=gpu --user=<CNetID>
```

??? tip
    You can customize the output of `squeue` and `sacct` by configuring your slurm environment variables:
    ```bash
    export SACCT_FORMAT="jobid,partition,user,account%12,alloccpus,node%12,elapsed,totalcpu,maxRSS,ReqM"
    export SQUEUE_FORMAT="%13i %12j %10P %10u %12a %8T %9r %10l %.11L %5D %4C %8m %N"
    squeue -u cnetid
    ```
    You can put the two export commands into a configuration bash file `set_slurm_env.sh` like [here](https://github.com/rcc-uchicago/R-large-scale/blob/master/set_slurm_env.sh){:target="_blank"}, and `source set_slurm_env.sh` before running `squeue`.


For more information, consult the command-line help by typing ```squeue --help```, or visit the [official online documentation](https://slurm.schedmd.com/documentation.html){:target="_blank"}.

### Canceling your jobs
To cancel a job you have submitted, use the ```scancel``` command. This requires you to specify the id of the job you wish to cancel. 

For example, to cancel a job with id 8885128, do the following:
```
scancel 8885128
```
If you are unsure what is the id of the job you would like to cancel, see the JOBID column from running ```squeue --user=<CNetID>```.

To cancel all jobs you have submitted that are either running or waiting in the queue, enter the following:
```
scancel --user=<CNetID>
```

### Monitoring Job Memory
You can monitor your job by connecting to the compute node it is running on via SSH and using the ```htop``` command.

To do this, run the following to see your running jobs and which compute nodes your jobs are running on:
```
squeue --state=RUNNING --user=<CNetID>
```
The last column of the output tells us which nodes are allocated for each job. You can connect to the compute node using the following command, where for example we are connecting to compute node midway2-0172.
```
ssh midway2-0172
```
Finally run:
```
htop
``` 
To view processes running on the node, including your job's process which will be listed under your CNetID in the USER column.
