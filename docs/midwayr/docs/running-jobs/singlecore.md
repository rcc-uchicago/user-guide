# Single core/thread sbatch job

To submit a single core/thread job to the scheduler, you will need to create a sbatch file
that requests this resource be scheduled and the workflow to be executed. 
The following sbatch script provides a minimal example of requesting a single 
node, single core job, which is the default when no other parameters are specified. 

```bash 

#!/bin/bash
#SBATCH --job-name=example_sbatch
#SBATCH --output=example_sbatch.out
#SBATCH --error=example_sbatch.err
#SBATCH --time=00:30:00

# LOAD THE MODULES REQUIRED FOR YOUR JOB
module load Anaconda3

# RUN JOB
python myjob.py 
```

In this minimal example sbatch script, only the wall time is passed to the 
scheduler. Since the quantity of nodes and cores/threads as well as memory were
not specified, the default values for each are provisioned by the scheduler. 

Once a core is available and is allocated to the job, the `myjob.py` python code
will then be executed on the allocated single core on one of the compute nodes.

Default resources allocated when not specified: 

|  |   Default |
|----|----|
|**Memory:**| 2000MB (2GB)|
|**Cores:**|  1 |
|**Walltime:**| 36 hours|


