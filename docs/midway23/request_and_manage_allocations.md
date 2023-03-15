## Checking Your SU Balance and Usage
The `rcchelp` tool can be used to check account balances. After logging into Midway 2 or Midway 3, simply type:
```
rcchelp balance
```

If you are a member of multiple groups, this will display the allocations and usage for all your groups. The rcchelp balance command has a number of options for summarizing allocation usage. For information on these options, type
```
rcchelp balance --help
```

To see an overall summary of your usage, simply enter:
```
rcchelp usage
```

You can also use the command `accounts` to show the current usage and other information. For instance, the following two useful commands
```
accounts usage --accounts pi-[PI-CNetID] --byuser
```
and
```
accounts usage --accounts pi-[PI-CNetID] --byjob
```
show the current SU usage of individual users, and of individual jobs under the given PI account, respectively.

For the complete list of available options for the command `accounts` you can simply run
```
accounts
```

!!! note
    There are certain differences in the arguments and output of the `accounts` and `rcchelp` commands on Midway2 and Midway3. Attempts to make them consistent are underway.