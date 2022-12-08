# MidwayBooth Data Transfer
This section of the documentation provides an overview of data transfer mechanisms for MidwayBooth. Please remember that MidwayBooth is a partition on the Midway3 cluster. The SSD has purchased storage for SSD faculty and student researchers; however, your storage is allocated on the Midway3 cluster. Therefore, the data transfer process described below is identical to the description for the Midway3 Intel and AMD partitions. Your storage is mounted to the greater cluster, allowing you to specify which partition you would like to use for your compute needs. 
RCC provides a number of methods for accessing and transferring data in/out of our systems.
We recommend the SCP protocol for transferring files to/from RCC systems.
RCC hosts a managed Globus Online endpoint that can be used for moving very large amounts of data.

## SSH (SCP or SFTP)
Secure copy or SCP is a means of securely transferring computer files between a local host and a remote host.
It is based on the Secure Shell (SSH) and Secure File Transfer (SFTP) protocols.

To transfer files or directories from your local computer to your home directory on Midway3, open a terminal window and issue the command:
```
$ scp <some file> <CNetID>@midway3.rcc.uchicago.edu:
```
Or for directories:
```
$ scp -r <some dir> <CNetID>@midway3.rcc.uchicago.edu:
```
Or to connect to a directory on Midway3 (/project, for example):
```
$ scp -r <some dir> <CNetID>@midway3.rcc.uchicago.edu:/project
```

## SAMBA
SAMBA allows uses to connect to (or “mount”) their home and project directories on their local computer so that the file system on Midway3 appears as if it were directly connected to the local machine.
This method of accessing your RCC home and project space is only available from within the UChicago campus network.
From off-campus you will need to first connect through the UChicago VPN.

Your SAMBA account credentials are your CNetID and password:
```
Username: ADLOCAL\CNetID
Password: CNet password
Hostname: midway3smb.rcc.uchicago.edu
```
**Note:** Make sure to prefix your username with `ADLOCAL\`

### Connecting from Windows
On a Windows computer, use the “Map Network Drive” option:
* Enter one of the following UNC paths depending on which location on Midway you wish to connect to:

```
home:     \\midway3smb.rcc.uchicago.edu\homes
project: \\midway3smb.rcc.uchicago.edu\project
scratch:  \\midway3smb.rcc.uchicago.edu\midway3-scratch
```
* When prompted for a username and password, select **Registered User**.
* Enter `ADLOCAL\CNetID` for the username and enter your CNet password.

### Connecting from Mac OS X
To connect on a Mac OS X computer follow these steps:

* Open the **Connect to Server** utility in Finder
* Enter one of the following URLs in the input box for **Server Address** depending on which location on Midway you wish to connect to:

```
home:            smb://midway3smb.rcc.uchicago.edu/homes
project:        smb://midway3smb.rcc.uchicago.edu/project
scratch/midway:  smb://midway3smb.rcc.uchicago.edu/midway3-scratch
```
* When prompted for a username and password, select **Registered User**.
* Enter `ADLOCAL\CNetID` for the username and enter your CNet password.

### Connecting from Ubuntu
From Ubuntu, follow the steps here: https://wiki.ubuntu.com/MountWindowsSharesPermanently. Specifically,

* Install cifs `sudo apt-get install cifs-utils`.
* Create a folder to contain the mounted filesystem, e.g. `mkdir /media/midway`
* Put your RCC credentials in a text file. Create a file `.smbcredentials` in your home directory containing:
```
username=[midway username]
password=[midway password]
```

* Change permissions so only you can read the file `chmod 600 ~/.smbcredentials`.
* Edit the file `/etc/fstab` as root and add the following on one line at the end (Note: You can change “project” in the below line to “homes”, “project2”, or “midway3-scratch” depending on which location you wish to mount):

```
//midway3smb.rcc.uchicago.edu/project2 /media/midway cifs credentials=/home/[username]/.smbcredentials,domain=ADLOCAL,iocharset=utf8,sec=ntlm,vers=2.0 0 0
```

* Remount everything in `/etc/fstab` with the command `sudo mount -a`.

Your Midway folders should now be accessible at `/media/midway`.


## HTTP (web access)
RCC provides web access to data on their storage system via `public_html` directories in users’ home directories.

Be sure your home directories and `public_html` have the execute bit set, and that `public_html` has read permissions if you would like to allow indexing (directory listings and automatic selection of index.html).
For example, these are the commands for setting up Web access to your home directory, where `$HOME` is the environment variable specifying the location of your home directory:
```
chmod o+x $HOME
mkdir -p $HOME/public_html
chmod o+x $HOME/public_html
chmod o+r $HOME/public_html
```
The last line is optional and only needed if you would like to allow directory listing.
Files in public_html must also be readable by the web user (other), but should not be made executable, e.g.,
```
chmod o+r $HOME/public_html/research.dat
```
**Note:** Use of these directories must conform with the RCC usage policy (<a href="https://rcc.uchicago.edu/about-rcc/rcc-user-policy" target="_blank">https://rcc.uchicago.edu/about-rcc/rcc-user-policy</a>).
Please notify RCC if you expect a large number of people to access data hosted here.


## Globus Online
Globus Online is a robust tool for transferring large data files to and from Midway3.

The RCC has a customized Globus Online login site at <a href="https://globus.rcc.uchicago.edu" target="_blank">https://globus.rcc.uchicago.edu</a> and uses the Single Sign On capabilities of CILogon.

Once you have signed up, here is the connection information for Midway3:
```
URL:       https://globus.rcc.uchicago.edu
End Point: ucrcc#midway3
```
For full instructions, please see <a href="https://rcc.uchicago.edu/docs/data-transfer/index.html#globus-online" target="_blank">Globus Online Data Transfer</a>.
