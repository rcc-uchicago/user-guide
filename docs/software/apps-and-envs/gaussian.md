# Gaussian

<a href='https://gaussian.com/g16main/' target='_blank'>Gaussian</a> is a computational chemistry software package available to RCC users for chemistry research.

## Get access

<p align='center'>
<img src='../img/software/gaussian-access.png'
width='650'
alt='A flowchart of steps for accessing Gaussian through the RCC. These steps are detailed below.'
longdesc='TXT'/>
</p>

**Step 1** If you are not already an RCC user, your first step is to become one. If you are a Principal Investigator (PI), submit a <a href='https://rcc.uchicago.edu/accounts-allocations/pi-account-request' target='_blank'>PI Account Request</a>. If you are a student, postdoc, staff member, etc., submit a <a href='https://rcc.uchicago.edu/accounts-allocations/general-user-account-request' target='_blank'>General User Account Request</a>.

**Step 2** To access Gaussian, you must be a member of the RCC's `gaussian` Unix group. You can check if you are already a member of the `gaussian` group by running `groups` in the terminal while connected to a Midway cluster login node. To join the `gaussian` group, submit a <a href='https://rcc.uchicago.edu/accounts-allocations/general-user-account-request' target='_blank'>General User Account Request</a> with "Gaussian" as the Principal Investigator account name. (Note that even PIs submit a General User Account Request to get access to Gaussian. This is different from Step 1, where PIs submit a PI Account Request to become an RCC user.)

Once you are a member of the `gaussian` group, you will be able to run Gaussian programs. To check what versions of Gaussian are currently available on the Midway clusters, use SSH to log into Midway2 or Midway3 and run this command in your terminal:

```
$ module avail gaussian
```

Note that the versions of Gaussian on Midway2 and Midway3 may be different; please check both of them if you need a specific version.

You can run Gaussian jobs in an [`sinteractive` session](../../slurm/sinteractive.md), meaning you connect live to a compute node, or by using an [`sbatch` script]() to send your job to a compute node. Gaussian jobs will only run on compute nodes, not login nodes.