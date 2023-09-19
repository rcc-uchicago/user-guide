#Common Mistakes to Avoid

1. **Do not go over your storage quota.**<br> Exceeding your storage quota can lead to many problems including batch jobs failing, confusing error messages, and the inability to use X11 forwarding. Be sure to routinely run the `rcchelp quota` command to check your usage. If more space is needed, then you can remove files to comply with number-of-files and size quotas or [request an allocation](../FAQ/data_management_faq.md). 
 
2. **Do not install conda environments using `conda create --name=<env_name>`.**<br> 
By default, this command will install a virtual conda environment into `/home` directory, which has a low quota. Because Anaconda environments often require a large amount of storage and number of files this may easily result in exceeding quota. Instead install virtual environments inside /project or /project2 directories by running `conda create --prefix=/project/<PI_CnetID>/<CNetID/anaconda/<env_name>`.

3. **Do not run jobs on the login nodes.**<br> 
When you connect to a cluster via SSH, you land on the login node, which is shared by all users. The login node is reserved for submitting jobs, compiling codes, installing software, and running short tests that use only a few CPU cores and finish within a few minutes. Anything more intensive must be submitted to the Slurm job scheduler as either a batch or interactive job. Failure to comply with this rule may result in your account being temporarily suspended.
 
4. **Do not try to access the Internet from batch or interactive jobs.**<br> 
All jobs submitted to the Slurm job scheduler run on the compute nodes that do not have Internet access. This includes ThinLinc sessions. Because of this, a running job cannot download files, install packages or connect to GitHub. Before submitting the job, you will need to perform these operations on the login node.
 
5. **Do not allocate more than one CPU core for serial jobs.**<br> 
Serial codes cannot run in parallel, so using more than one CPU core will not cause the job to run faster. Instead, doing so will waste SUs allocated to your PI. See [tips](../midway23/examples/example_job_scripts.md) on figuring out if your code can run in parallel and for information about Job Arrays, which allow one to run many jobs simultaneously.
 
6. **Do not run jobs with a parallel code without first conducting a scaling analysis.**<br>
If your code runs in parallel then you need to determine the optimal number of nodes and CPU-cores to use. The same is true if it can use multiple GPUs. To do this, perform a scaling analysis.
 
7. **Do not request a GPU for a code that can only use CPUs. Only codes that have been explicitly written to use GPUs can take advantage of GPUs.**<br> 
Allocating a GPU for a CPU only code will not speed up the execution time but it will increase your queue time, waste resources and lower the priority of your next job submission. Furthermore, some codes are written to use only a single GPU.
 
8. **Do not use the system GCC when a newer version is needed**<br>
The GNU Compiler Collection (GCC) provides a suite of compilers (gcc, g++, gfortran) and related tools. You can determine the version of the system GCC by running the command "gcc --version". If the system version is insufficient then load the appropriate environment module to make a newer version available. Run the command "module avail gcc". Learn more about [environment modules](../midway23/software/midway_software_overview.md).
 
9. **Do not load environment modules using only the partial name.**<br>
A common practice for Python users is to issue the "module load python" command. You should always specify the full name of the environment module (e.g., module load python/anaconda-2022.05) to make sure the default version hasn't changed. Also, you should avoid loading environment modules in your ~/.bashrc file. Instead, do this in Slurm scripts and on the command line when needed.
 
10. **Do not write temporary files to `/scratch` if your job has high throughput I/O **<br>
Temporary files may accumulate and exceed your quota (both in terms of size and/or number of files) unless removed on time. If your job is not distributed across multiple nodes and has high throughput I/O of many small files (size < 4 MB), you may have faster performance when writing temporary files to the [local scratch compared to the shared scratch](../midway23/midway_data_storage.md). However, the local scratch is not justified if your temporary files exceed the local scratch space. 

11. **Do not compile and install heavy software using login nodes**<br>
Sometimes software installation time can be dramatically reduced by using multiple cores. However, compute-intensive jobs are not permitted on login nodes and may be killed to provide equal opportunities for other connected users. Instead of login nodes, use a build partition, which is dedicated to software installation.