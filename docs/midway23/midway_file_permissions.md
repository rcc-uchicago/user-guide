# File System Permissions and Sharing

## File Permissions

Linux divides file permissions into read, write and execute (denoted by `r`, `w`, and `x`) for three user types: `Owner`, `Group`, and `Other`. Here is how you interpret this in the command line:

<img src="../img/Files-permissions-and-ownership-basics-in-Linux.png" width="400" height="250" />

To represent a given file's permissions for the three user types, combinations of the letters are commonly [represented by numbers](https://www.guru99.com/file-permissions.html#absolute_mode_in_linux){:target="_blank"} (i.e., 0700).  

Let’s first summarize the default file system permission on Midway:

| Directory               | Permissions                               |
|-------------------------|-------------------------------------------|
| `$HOME`                 | `0700` – Accessible only to the owner     |
| `$SCRATCH`              | `0700` – Accessible only to the owner     |
| `/project/<PI CNetID>`  | `2770` – Read/write for the project group |
| `/project2/<PI CNetID>` | `2770` – Read/write for the project group |

The default umask is `002`. When new files or directories are created, the umask
influences the default permissions of those files and directories.  With the
umask set to `002` all files and directories will be group readable and
writable by default. In your home directory, the group ownership will be set
to your personal group, which is the same as your CNetID, so you will still
be the only user that can access your files and directories. In the project
directories, the group sticky bit causes the group ownership to be the same
as the directory. This means files created in a project directory will be
readable and writable by the project group, which is typically what is wanted
in those directories.

Here is an example of what this means in practice:

```default
$ ls -ld $HOME /project/rcc
drwx------ 108 wettstein wettstein 32768 2013-01-15 10:51 /home/wettstein
drwxrws---  24 root      rcc-staff 32768 2013-01-15 10:48 /project/rcc
$ touch $HOME/newfile /project/rcc/newfile
$ ls -l /project/rcc/newfile $HOME/newfile
-rw-rw-r-- 1 wettstein wettstein 0 2013-01-15 10:48 /home/wettstein/newfile
-rw-rw-r-- 1 wettstein rcc-staff 0 2013-01-15 10:48 /project/rcc/newfile
```

Both files are readable and writable by the group owner due to the default
umask, but the group owner differs due to the sticky bit being set on
`/project/rcc`.  

!!! note
      This applies only to newly created files and directories. If files or directories are moved from elsewhere, the ownership and permission may not work like this. Contact RCC help if you need assistance with setting filesystem permissions.
   
   
## Advanced Access Control via ACL

Access control lists [(ACL)](https://www.redhat.com/sysadmin/linux-access-control-lists) provides an additional, more flexible permission mechanism for file systems. It is designed to assist with UNIX file permissions. ACL allows you to give permissions for any user or group to any disk resource. For more information, please visit the ACL manual at [https://wiki.archlinux.org/index.php/Access_Control_Lists](https://wiki.archlinux.org/index.php/Access_Control_Lists)

!!! note
      At present ACL is only available on Midway2.

### General Instructions

This section discusses a more flexible mechanism to administer data permissions. By default, only Linux-based permissions are set for folders and files, as described in File System Permissions. However, this only supports the permissions at the owner/group/others level. A second mechanism is called “Access Control Lists” (ACL), which provides precise control over any data (files or directories) customizable for individual users or groups. Before applying ACL to your data, please read and understand the following caveats.


* By default no ACL is set for user data. ACL provides a highly flexible permission control, however, it also brings increased complexity to user access and management. PIs will normally want to share an entire project folder to all group members, and for this, the Linux-based permissions are enough. We suggest that users implement ACL controls only when necessary. One example is to protect confidential data in the project space by allowing only certain users to access confidential directories or files.


* After ACL is set, both Linux-based and ACL permissions will work together as a dual-guard system. The final effective access to data is granted only if permitted by both mechanisms. For example, if a folder is group-accessible to a user by Linux-based permission but restricted by ACL, the user cannot access this folder.


* Be sure you have enough knowledge setting up access via Linux-based permissions and ACL, i.e. you understand what “users”, “groups” and each attribute in “rwx” mean and how to use them. Otherwise, please [contact our Help Desk](https://rcc.uchicago.edu/support-and-services/consulting-and-technical-support){:target="_blank"} for assistance managing your data access. We are here and happy to help you set up the permissions to keep your data safe and accessible as required.

### Examples

#### Sharing folders with a user within a group
Suppose there is a folder tree as below, and you want to allow the folder `my_folder` to be accessible by the user `jim` only,
and `jim` is already a member of your group `rcctemp1`:

```default
/project2/rcctemp1
   |- my_folder
   |- other_stuff
```

Before using ACL, you need to confirm that this folder is permitted by all members in the group `rcctemp1`:

```default
$ cd /project2
$ chgrp -R rcctemp1 my_folder
$ chmod -R 770 rcctemp1
$ cd rcctemp1
```

At this moment, the folder `rcctemp1` becomes readable and writable by all members of group `rcctemp1`. Then, you can use
the `setfacl` command to control the individual users access precisely. First, you need to remove the default group
access by ACL:

```default
$ setfacl -m g::--- my_folder
```

Although the command `ls -l` will still display group `rwx` access for the `my_folder` folder in the Linux-based permissions,
users cannot access it anymore due to the permission set by ACL. Then, you can grant the user `jim` access to the folder:

```default
$ setfacl -m u:jim:rwx my_folder
```

At this step, the user `jim` has both read and write permissions to the folder `my_folder`. You can set up permissions for
each user the way you want.

To view the list of configured accesses on the folder `my_folder`, run:

```default
$ getfacl my_folder
# file: my_folder
# owner: root
# group: rcctemp1
user::rwx
user:jim:rwx
group::---
mask::rwx
other::---
```

To revoke the permissions of the user `jim` to the folder:

```default
$ setfacl -x u:jim my_folder
```

To clean up (remove) all ACL controls to the folder:

```default
$ setfacl -b my_folder
```

#### Sharing folders with a user outside a group

Suppose you would like to share your folder `/project2/pi-cnetid/my_own_folder/shared_data` with another RCC user with CNetID `coworkerA`, who is not in your group `pi-cnetid`. As the owner of the folder, you can execute the following two commands
```
setfacl -Rm d:u:coworkerA:rw-,u:coworkerA:rw- /project2/pi-cnetid/my_own_folder/shared_data
setfacl -m u:coworkerA:--x /project2/pi-cnetid/my_own_folder
```
The first command changes the ACL permission of the folder (and recursively its sub-folders and files) to allow the user `corworkerA` to read and write. The second command adds execute permission to `coworkerA` so that `coworkerA` can access the parent folder `/project2/pi-cnetid/my_own_folder` but without read nor write permissions.

