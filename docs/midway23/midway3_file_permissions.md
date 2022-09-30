# File System Permissions

Let’s summarize the default file system permissions:

| Directory | Permissions |
| --------- | ----------- |
| `$HOME`| `0700` – Accessible only to the owner|
| `$SCRATCH`| `0700` – Accessible only to the owner|
| `/project/<PI CNetID>`| `2770` – Read/write for the project group|
| `/project2/<PI CNetID>`| `2770` – Read/write for the project group|

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

**NOTE**: This applies only to newly created files and directories. If files or directories are moved from elsewhere, the ownership and permission may not work like this.  Contact RCC help if you need assistance with setting filesystem permissions.