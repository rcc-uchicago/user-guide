# [CESM](single:CESM)

CESM can be built and run on Midway.  For more information about CESM and how to acquire the source code, see [http://www.cesm.ucar.edu/](http://www.cesm.ucar.edu/)

To date, CESM versions 1.0.4 and 1.1.1 have been run on Midway.  The port validation procedure has been completed for CESM version 1.0.4 in conjunction with the Intel compiler suite version 12.1.  Port validation results were found to be within tolerances (documentation coming soon).

RCC has also downloaded the entire CESM inputdata repository and maintains a local copy.  This can be found at `/project/databases/cesm/inputdata`.

We recommend using the intel compiler suite with CESM.  The relevant modules that need to be loaded when working with CESM are therefore:

```bash
$ module load intelmpi
$ module load netcdf/4.2+intel-12.1
```

To configure CESM on Midway, download the CESM source and insert the following configuration files for the specific version of CESM you are using into your local copy of CESM.

## CESM 1.0.4

These files should be placed in `/path/to/cesm1_0_4/scripts/ccsm_utils/Machines/` (overwriting the default files)

`cesm1_0_4/Macros.midway`

`cesm1_0_4/mkbatch.midway`

`cesm1_0_4/env_machopts.midway`

`cesm1_0_4/config_machines.xml` – see note about how to edit this file

You will need to edit your copy of config_machines.xml to point to appropriate locations.  On lines 7 and 13, replace the substring “/path/to/cesm1_0_4” with the path to your local installation of CESM 1.0.4

Once you have edited and inserted these files, you can run an example model with CESM 1.0.4 by running the following script (take note to edit the first line to point to your local installation of CESM 1.0.4):

`cesm1_0_4/example.sh`

## CESM 1.1.1 and CESM 1.2.1

These files should be placed in `/path/to/cesm1_1_1/scripts/ccsm_utils/Machines/` (overwriting the default files)

`cesm1_1_1/config_compilers.xml`

`cesm1_1_1/mkbatch.midway`

`cesm1_1_1/env_mach_specific.midway`

`cesm1_1_1/config_machines.xml` – see note about how to edit this file

You will need to edit your copy of config_machines.xml to point to appropriate locations.  On lines 59, 60, and 63, replace the substring “/path/to/cesm1_1_1” with the path to your local installation of CESM 1.1.1

Once you have edited and inserted these files, you can run an example model with CESM 1.1.1 by running the following script (take note to edit the first line to point to your local installation of CESM 1.1.1):

`cesm1_1_1/example.sh`
