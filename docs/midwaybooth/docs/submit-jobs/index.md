# Submitting Jobs on MidwayBooth using the Slurm Batch Scheduler

A batch job is a compute task that you would like to schedule to run on MidwayBooth without your active participation in the session. Often these are tasks designed to utilize multiple cores in a parallel fashion to help enhance the compute efficiency of your job. Running a scheduled job on the compute nodes means that you request resources on MidwayBooth and the Slurm job scheduler allocates your requested resources while balancing the job requests of other authorized users. This ensures the efficient and fair utilization for all MidwayBooth users. Please remember that you will not be able to run jobs that require internet connectivity on the compute nodes. 

## Running Jobs on a Compute Node

You may request resources to run your job on a compute node through either ThinLinc or SSH. You will select the resources that you require and be notified upon job completion by an automated systems message to your email. If you choose to submit a job via ThinLinc, you will do this by selecting the Slurm Icon and following the prompts in the dialog box to choose the resources that you require and account under which you are currently working. If you prefer to submit a batch script via SSH, this is done from the terminal prompt on your local machine. Please connect first via ssh and follow the recommendations for writing this script as indicated below.

## Requesting Resources for Your Job

If no wall time is specified in the resource request it will default to the 36 hour max wall time limit. An example sbatch resource request script for a 2 node, 80 core, mpi parallel job that uses the MidwayBooth partition is shown below.

```
#!/bin/bash
#SBATCH --time=1-12:00:00 
#SBATCH --partition=ssd
#SBATCH --account=pi-name      # You must specify the pi-account you are running under
#SBATCH --nodes=2              # Number of nodes
#SBATCH --ntasks-per-node=40   # Number of tasks
#SBATCH --cpus-per-task=1      # Number of threads per task
#SBATCH --qos=MidwayBooth        # QOS 

#
# SET NUM TASKS 
NTASKS=$(($SLURM_NTASKS_PER_NODE * $SLURM_JOB_NUM_NODES))

#
# SET NUMBER OF THREADS 
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

#LOAD MODULES (e.g. intelmpi)
module load  intelmpi/2018.2.199+intel-18.0

# EXECUTE JOB
mpirun -np $NTASKS myjob.x

#
# EOF
```
