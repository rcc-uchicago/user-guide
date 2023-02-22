# Introduction to RCC for MSc in Analytics

As a student in the Master of Science in Analytics (MScA) Program, you will be able to make use of The University of Chicago’s Research Computing Center (RCC) resources in completing your capstone project.  Some courses in the program will also make use of RCC resources.

RCC provides high-end research computing resources to researchers at the University of Chicago. These resources include centrally managed high-performance computing, storage, and visualization hardware, software, scientific and technical user support, as well as education and training opportunities to help researchers effectively make use of modern HPC technology.  To learn more about RCC, see [https://rcc.uchicago.edu](https://rcc.uchicago.edu).

Below are the basics you will need to know in order to get up and running at RCC.  For complete RCC technical documentation, see the main sections of this user guide. 

## Getting Help

RCC support staff is available to assist with technical issues (help logging in, questions about using the cluster, etc).  Please don’t hesitate to ask questions if you encounter any technical issues.


* The preferred way of requesting support is to send an email request to [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu)


* RCC’s walk-in lab is open during business hours and is located in Regenstein Library room 216. Feel free to drop by to chat with one of our staff members if you get stuck.


* The RCC helpdesk can be also reached by phone at 773-795-2667 during normal business hours.

## Logging into Midway

For the most complete documentation regarding connecting to RCC resources see: [Connecting to RCC Resources](../../connecting/index.md#connecting).

### Credentials

All users must have a UChicago [CNetID](https://itservices.uchicago.edu/services/cnetid) to log in to any RCC system. Your RCC account uses the same username/password as your CNetID:

```default
Username: CNetID
Password: CNet password
```

Upon acceptance into the MScA program, a RCC user account will automatically be activated for you.  If all has gone according to plan, there is no action required to obtain an RCC user account.  However, if for whatever reason you believe your account has not been activated, please contact [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu)

**NOTE**: RCC does not store your CNet password and we are unable to reset your password.
If you require password assistance, please see the [CNet Password Recovery](https://cnet.uchicago.edu/recertify/) webpage.

### 2-Factor Authentication

Follow the instructions on [https://2fa.rcc.uchicago.edu](https://2fa.rcc.uchicago.edu) to enroll into 2fa.

### Connecting with SSH

Access to RCC resources is provided via secure shell (SSH) login.  Most Unix-like operating systems (Mac OS X, Linux, etc) provide an ssh utility by default that can be accessed by typing the command **ssh** in a terminal window.

To login to midway2 from a Linux or Mac computer, open a terminal and at the command line enter:

```default
$ ssh <CNetID>@midway2.rcc.uchicago.edu
```

Windows users will first need to download an ssh client, such as [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) or 

```
MobaXterm_
```

, which will allow you to interact with the remote Unix command line. Use the following information to set up your connection:

```default
Hostname: midway2.rcc.uchicago.edu
Username: CNetID
Password: CNet password
```

### Connecting with ThinLinc

ThinLinc is a remote desktop server that can be used to connect to RCC systems and obtain a remote graphical user interface (GUI). RCC recommends that ThinLinc be used when running software that requires a GUI.

**NOTE**: You can connect to RCC systems via the ThinLinc web client at [https://midway2.rcc.uchicago.edu](https://midway2.rcc.uchicago.edu). The performance will be slower, but no client download is necessary.

There are some differences between the Mac OS X, Windows, and Linux clients, but for the most part, these steps should be followed:


* Download and install the appropriate ThinLinc client here:
[https://www.cendio.com/thinlinc/download](https://www.cendio.com/thinlinc/download)


* Open the ThinLinc client and use the following information to set up your connection:

```default
Server: midway2.rcc.uchicago.edu
Username: CNetID
Password: CNet password
```

Your client should look similar to this:



![image](./img/thinlinc-client.png)


* The default setting for ThinLinc is for the client to open in a fullscreen window that fills “all monitors.” If you would prefer to work with ThinLinc from its own window, click *Options* from the initial login interface and then *Screen* to adjust your settings as desired. The following is an example of a setup that places the ThinLinc client in its own window:



![image](./img/thinlinc-options.png)


* *Optional*: You are also able to export local resources via ThinLinc. To do so, click *Options* from the initial login interface and then *Local Devices*. To adjust your settings for exporting the local file system, click *Details* next to *Drives*.



![image](./img/thinlinc-local-resources.png)


* Upon successfully logging in, you will be presented with an gnome desktop.
Click with right mouse button anywhere on the desktop and select “Open Terminal” from the menu.



![image](./img/thinlinc-desktop.png)

With ThinLinc it is possible to maintain an active session after you have closed your connection to Midway.  To disconned from Midway but maintain an active session (e.g. when you log back into the ThinLinc client you will resume your remote session from where you left off), simply close the ThinLinc window. NOTE: You must have *End existing session* **unchecked** for this to occur.

To exit ThinLinc and terminate your session completely, simply select *Logout* from the *Applications* menu.

## Using the Midway Cluster

The Midway compute cluster is a shared resource used by the entire University community. Sharing computational resources creates unique challenges:


* Jobs must be scheduled in a fair manner.


* Resource consumption needs to be accounted.


* Access needs to be controlled.

Thus, a **scheduler** is used to manage job submissions to the cluster.  RCC uses the [Slurm](http://slurm.schedmd.com) resource manager to schedule jobs and provide interactive access to compute nodes.

For detailed information on running specific types of compute jobs, consult the pages [Using Midway](../../using-midway/index.md#using-midway) and [Running jobs on midway](../../running-jobs/index.md#running-jobs).  Software-specific information can be found on the RCC [Software](../../software/index.md#software) page.

## Data Transfer, Storage, and Backup

RCC maintains a petascale high-performance GPFS shared file system which is used for users’ home directories, shared project space, and high-throughput scratch space.

### Transferring files

RCC provides a number of methods for accessing and transferring data in/out of our systems. We recommend the scp protocol for transferring files to/from RCC systems. RCC hosts a managed Globus Online endpoint that can be used for moving very large amounts of data. When connecting from the UChicago network or through the UChicago VPN it is also possible to connect to the RCC file systems using SAMBA.

Please see the [Data Transfer](../../data-transfer/index.md#data-transfer) page for more information on how to move files to/from Midway.

### Persistent and Temporary Storage

You will have access to three different storage locations on Midway.

All users are given a home directory with a 30GB quota.  This location should be used for small files, code, etc.  It is located at `/home/$USER`.

For large capacity storage, MScA has obtained a block of high-capacity storage located at `/project/msca/`.  Each MScA user is initially given a 10GB quota on their own subdirectory (`/project/msca/$USER)`.  If you require more space, please contact Gregory Guevara <[gguevara@uchicago.edu](mailto:gguevara@uchicago.edu)> with a description of your requirements and an estimate of how much storage you will require.  Storage quotas in `/project/msca` will be increased on a case-by-case basis and may require a monetary contribution by the user.

Finally, you will have access to a high-performance filesystem mounted on `/scratch/midway2/$USER` which has a 100GB quota. This storage location is intended for SHORT-TERM STORAGE ONLY.

**NOTE**: Your scratch directory is NOT backed up and should NOT be used for long-term storage. Files stored in your scratch space that are older than 2 weeks may be removed automatically, so please practice good data management.

### Backups and Snapshots

We all inadvertently delete or overwrite files from time to time.  Snapshots are automated backups that are accessible through a separate path.  Snapshots of a user’s home directory can be found in `/snapshots/\*/home/$USER/` where the subdirectories refer to the frequency and time of the backup, e.g. daily-2012-10-04.06h15 or hourly-2012-10-09.11h00.  More information about backups can be found in the [Snapshots](../../data-storage/index.md#snapshots) section of the [Data Storage](../../data-storage/index.md#data-storage) page.

While snapshots are the preferred way to recover lost files, RCC also maintains an archival tape backup of data stored in `/project` and `/home` file systems for disaster recovery purposes only.

## Software

Many commonly used software packages and libraries have been installed on Midway for your use.  See the complete [Software Module List](../../software/modules/index.md#modules) for a list of all software installed on Midway.  For an overview of how to use Software Modules on Midway, consult the RCC [Software](../../software/index.md#software) documentation page.

## SAS

SAS Studio is available to MScA students. SAS Studio is a web application
frontend to SAS. To access SAS Studio, visit this link and log in with your
CNetID and password:

[https://sas-studio.rcc.uchicago.edu](https://sas-studio.rcc.uchicago.edu)

Also, an instance of SAS Enterprise Miner is available to MScA students.  To access SAS Enterprise Miner, you can visit this link:

[https://sas-miner.rcc.uchicago.edu:8343/SASEnterpriseMinerJWS/Status](https://sas-miner.rcc.uchicago.edu:8343/SASEnterpriseMinerJWS/Status)

SAS software is also available on Midway.  To load the SAS software module, use the command `module load sas`. It is recommended to use ThinLinc as described above to login to Midway if you want to use SAS in this manner.

## Nielsen Data

The MScA program has obtained a subset of the Nielsen Homescan data for use in teaching and research projects.  Access to this data is controlled by MScA administration.  If you require access to this data, please consult your instructor or the MScA director and request that you be approved for access to the data.

Once your user account has been approved for access to the Nielsen data, you will be able to access the data in the directory `/project/msca/data/nielsen/` on Midway.
