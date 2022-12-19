# Frequently Asked Questions

## General 
### How do I cite RCC in my publications and talks?
Citations and acknowledgements help the RCC demonstrate the importance of computational resources and support staff in research at the University of Chicago. We ask that an acknolwedgment be given to the RCC in any presentation or publication of results that were made possible by RCC resources. Please reference the RCC as “The University of Chicago Research Computing Center” in citations and acknowledgements. Here are a few examples of suggested text:

This work was completed in part with resources provided by the University of Chicago Research Computing Center.

We are grateful for the support of the University of Chicago Research Computing Center for assistance with the calculations carried out in this work.

We acknowledge the University of Chicago Research Computing Center for support of this work.

If you cite or acknowledge the RCC in your work, please notify the RCC by sending an email to info@rcc.uchicago.edu.

## Getting Started
### How do I become an RCC user?
RCC user account requests should be submitted via our online application forms. See RCC Account Request for more information.

### How do I access RCC systems?
There are various ways to access RCC systems.

To access Midway2 interactively, use ThinLinc or an SSH client. See Connecting to RCC Resources for details.

To access files stored on Midway2, use scp, Globus Online or SAMBA. See Data Transfer for details.

### How do I request access to a PI’s account if I already have an account on Midway?
Please submit a User Account Request and provide your CNetID and the PI Account name (typically pi- followed by the CNetID of the PI). The PI will receive an automated email requesting authorization for this request.

### What is my RCC username and password?
The RCC uses the University of Chicago CNetIDs for user credentials. Once your RCC account is created, your RCC username and password will be the same as your CNetID credentials.

### Can an external collaborator get a CNetID so they can log in to RCC?
The RCC can create CNetIDs for external collaborators. See RCC Account Request for more information.

### What should I do if I left the university and my CNetID password no longer works?
You can use your CNetID for authentication after you have left, but IT Services may expire it when you leave. If you have an RCC account, but you still can’t log in, it is likely that password authentication has been disabled by IT Services. Please contact help@rcc.uchicago.edu to request re-enabling access to your account.

### How do I change/reset my password?
The RCC cannot change or reset your password. Go to the CNet Password Recovery page to change or reset your password.

### What groups am I a member of?
To list the groups you are a member of, type groups on any RCC system.

### How do I access the data visualization lab in the Zar room of Crerar Library?
The Zar room and its visualization equipment can be reserved for events, classes, or visualization work by contacting the RCC at help@rcc.uchicago.edu. More information regarding the RCC’s visualization facilities can be found on the RCC Data Visualization page.

### What login shells are supported and how do I change my default shell?
The RCC supports the following shells:
```
/bin/bash
/bin/tcsh
/bin/zsh
```
Use this command to change your default shell:


``` 
chsh -s /path/to/shell 
```

It may take up to 30 minutes for that change to take effect.

### Is remote access with Mosh supported?
Yes. To use Mosh, first log in to Midway via SSH, and add the command module load mosh to your ```~/.bashrc``` (or ```~/.zshenv``` if you use zsh). Then, you can log in by entering the following command in a terminal window:


``` 
mosh <CNetID>@midway2.rcc.uchicago.edu 
```

### Is SSH key authentication allowed on RCC machines?
No, SSH key authentication is not allowed.

### Why am I getting “ssh_exchange_identification: read: Connection reset by peer” when I try to log in via SSH ?
You can get this error if you incorrectly enter your password too many times. This is a security measure that is in place to limit the ability for malicious users to use brute force SSH attacks against our systems.

After 3 failed password entry attempts, an IP address will be blocked for 4 hours.

While you wait for the block to be lifted, you should still be able to access Midway2 using ThinLinc.

### Why am I getting prompted for YubiKey when I try to log in via SSH ?
There are few reasons to get that error message. Please enroll in two factor authentication if you have not done already by visiting https://2fa.rcc.uchicago.edu. Please make sure you run ssh -Y your_cnetID@midway2.rcc.uchicago.edu. Finally, please make sure your Midway account has not been expired.

## Allocations
### What is an allocation?
An allocation is a specified number of computing and storage resources granted to a PI or education account. An allocation is necessary to run jobs on RCC systems. See RCC Allocations for more details.

### What is a service unit (SU)?
A service unit (SU) is roughly equal to 1 core-hour; for a more precise definition, see RCC Service Units.

### How do I obtain an allocation?
The RCC accepts proposals for large (“Research II”) allocations bi-annually. Medium-sized allocations, special purpose allocations for time-critical research, and allocations for education and outreach may be submitted at any time. See RCC Allocations for more information.

### How is compute cluster usage charged to my account?
The charge associated with a job on Midway2 is a function of (1) the number of cores allocated to the job, and (2) the elapsed wall-clock time (in hours).

How do I check the balance of my allocation?
The rcchelp tool is the easiest way to check your account balance.


``` 
rcchelp balance 
```
How do I check how my allocation has been used?
The rcchelp tool has several options for summarizing allocation usage. For a summary, run


```
rcchelp usage
```
To see usage per job, run


```
rcchelp usage --byjob
```
If you are the PI, you may use --byuser option to see your group members’ individual usage


```
rcchelp usage --byuser
```
## Software
### What software does RCC offer on its compute systems?
Software available within the RCC environment is constantly evolving. We regularly install new software, and new versions of existing software. Information about available software and how to use specific software pacakges can be found in the Software section of the User Guide.

To view the current list of installed software on Midway2, run

```
 module avail
```
To view the list of available versions for a specific software, run


``` 
module avail <software>
```
How do I get help with RCC software?
Documentation for many program can be viewed with the following command.


``` 
man <command>
```
Many programs also provide documentation through command-line options such as --help or -h. For example,


$ module load gcc
$ gcc --help
RCC also maintains supplementary documentation for software specific to our systems. Consult the Software page for more information.

### Why is my favorite command not available?
Most likely it is because you have not loaded the appropriate software module. Most software packages are only available after first loading the appropriate software module. See Software for more information on how to access pre-installed software on RCC systems.

### Why do I get an error that says a module cannot be loaded due to a conflict?
Occassionally, modules are incompatible with each other and cannot be loaded simultaneously. The module command typically gives you hints about which previously loaded module conflicts with the one you are trying to load. If you see such an error, try unloading a module with this command:


$ module unload <module-name>
How do I request installation of a new or updated software package?
Please send email to help@rcc.uchicago.edu with the details of your software request, including what software package you need and which version of the software you prefer.

### Why can’t I run Gaussian?
Gaussian’s creators have historically had a strict usage policy, so we have limited its availability on RCC systems. If you need to use Gaussian for your research, please contact help@rcc.uchicago.edu to request access.

## Cluster Usage
How do I submit a job to the queue?
RCC systems use Slurm to manage resources and job queues. For advice on how to run specific types of jobs, consult the Running jobs on midway section of the User Guide.

### Can I login directly to a compute node?
You can start up an interactive session on a compute node with the sinteractive command. This command takes the same arguments as sbatch. More information about interactive jobs, see Interactive Jobs.

### How do I run jobs in parallel?
There are many ways to configure parallel jobs—the best approach will depend on your software and resource requirements. For more information on two commonly used approaches, see Parallel batch jobs and Job arrays.

### Are there any limits to running jobs on Midway2?
Run rcchelp qos on Midway to view the current criteria.

### I am a member of multiple accounts. How do I choose which allocation is charged?
If you belong to multiple accounts, jobs will get charged to your default account unless you specify the --account=<account> option when you submit a job with sbatch.

Run this command to determine your default account.


sacctmgr list user $USER
To change your default account, run this command.


sacctmgr modify user $USER set defaultaccount=<account>
Alternatively, you may request the change by contacting the RCC.

### Why is my job not starting?
This could be due to a variety of factors. Running squeue --user=<userid> can will help to find the answer; see in particular the NODELIST(REASON) column in the squeue output. A job that is waiting in the queue may show one of the following labels in this column:

(Priority): Other jobs currently have higher priority than your job.

(Resources): Your job has enough priority to run, but there aren’t yet enough free resources to run it.

(QOSResourceLimit): Your job exceeds the QOS limits. The QOS limits include wall time, number of jobs a user can have running at once, number of nodes a user can use at once, and so on. For example, if you are at or near the limit of number of jobs that can be run at once, your job will become eligible to run as soon as other jobs finish.

Please contact RCC support if you believe that your job is not being handled correctly by the Slurm queuing system.

Also, note that if you see a large number of jobs that aren’t running when many resources are idle, it is possible that RCC staff have scheduled an upcoming maintenance window. In this case, any jobs requesting a wall time that overlaps with the maintenance window will remain in the queue until after the maintainence period is over. The RCC staff will typically notify users via email prior to performing a maintenance and after a maintenance is completed.

### Why does my job fail after a few seconds?
This is most likely because there is an error in your job submission script, or because the program you are trying to run is producing an error and terminating prematurely.

If you need help troubleshooting the issue, please send your job submission script, as well as the error generated by your job submission script, to help@rcc.uchicago.edu.

### Why does my job fail with message “exceeded memory limit, being killed”?
On the main midway2 partition, broadwl, Slurm allocates 2 GB of memory per allocated CPU by default. If your computations require more than the default amount, you should adjust the memory allocated to your job with the --mem or --mem-per-cpu flags. For example, to request 10 cores and 40 GB of memory on a broadwl node, include these options when running sbatch or sinteractive: --ntasks=1 --cpus-per-task=10 --mem=40G.

### Why does my sinteractive job fail with “Connection to closed.”?
There are two likely explanations for this error.

One possibility is that you are over the time limit. The default walltime for sinteractive is 2 hours. This can be increased by including the --time flag to your sinteractive call.

Another possiblity is that your job exceeded the memory limit. You can resolve this by requesting additional memory using --mem or --mem-per-cpu.

### How do I run jobs that need to run longer than the maximum wall time?
The RCC queuing system is designed to provide fair resource allocation to all RCC users. The maximum wall time is intended to prevent individual users from using more than their fair share of cluster resources.

If you have specific computing tasks that cannot be solved with the current constraints, please submit a special request for resources to help@rcc.uchicago.edu.

### Can I create a cron job?
The RCC does not support users creating cron jobs. However, it is possible to use Slurm to submit “cron-like” jobs. See Cron-like jobs for more information.

## Performance and Coding
### What compilers does the RCC support?
The RCC supports the GNU, Intel, PGI and NVidia’s CUDA compilers.

### Which versions of MPI does RCC support?
The RCC maintains OpenMPI, IntelMPI, and MVAPICH2 compilers. See Message Passing Interface (MPI) for more information and instructions for using these MPI frameworks.

### Can the RCC help me parallelize and optimize my code?
The RCC support staff are available to consult with you or your research team to help parallelize and optimize your code for use on RCC systems. Contact the RCC staff at help@rcc.uchicago.edu to set up a consultation.

### Does RCC provide GPU computing resources?
Yes. The RCC high-performance systems provide GPU-equipped compute nodes. For instructions on using the GPU nodes, see GPU jobs.

## File I/O, Storage, and Transfers
### How much storage space do I have?
Use the quota command to get a summary of your current file system usage and available storage space.

### How do I get my storage quota increased?
Additional storage space can be purchased through the Cluster Partnership Program. You may also request additional storage as part of a Research II Allocation or Special Allocation.

### How do I share files with others?
The recommended way to share files with members of your group is to store them in the /project or /project2 directory for your group. Project directories are created for all PI and project accounts. File and directory permissions can be customized to allow access to users within the group, as well as RCC users that do not belong to your group.

### I accidentally deleted or lost a file. How do I restore it?
The best way to recover a recently deleted, corrupted or lost file is from a snapshot. See Data Recovery and Backups for more information.

### How do I request a restore of my files from tape backup?
The RCC maintains tape backups of all home and project directories. These tape backups are intended for disaster recovery purposes only. There is no long-term history of files on tape. In most cases, you should use file system snapshots to retrieve recover files. See Data Recovery and Backups for more information.