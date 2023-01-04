# [CCSM3](single:CCSM3)

CCSM3 can be built and run on Midway.  For more information about CESM and how to acquire the source code, see [http://www.cesm.ucar.edu/models/ccsm3.0/](http://www.cesm.ucar.edu/models/ccsm3.0/)

We recommend using the intel compiler suite with CCSM3.  The relevant modules that need to be loaded when working with CESM are therefore:

```bash
$ module load intelmpi/4.1+intel-12.1
$ module load netcdf/4.2+intel-12.1
```

To provide users with a starting point in getting CCSM3 running on Midway, we provide here a version of CCSM3 which contains copy of CCSM3 that was downloaded on October 20, 2014 and has been modified to work on Midway.

**NOTE**: CCSM3 has not been validated on Midway and RCC strongly reccomends that users perform numerical validation tests before completing production runs on Midway.  The options set in these files (especially env.linux.midway) may not be optimal for your particular use case.  We strongly reccomend that you downlaod CCSM3 from [http://www.cesm.ucar.edu/models/ccsm3.0/](http://www.cesm.ucar.edu/models/ccsm3.0/) and move the modified files into your instance of the software one by one and take time to understand the changes/additions that were made.

Many of the edits in the following version of CCSM3 were inspired by following the documention on this site: [http://nf.nci.org.au/facilities/software/CCSM3/CCSM3_ac.html](http://nf.nci.org.au/facilities/software/CCSM3/CCSM3_ac.html)

`ccsm3_0-midway.tar` contains all of the files distributed with CCSM3 as of October 20, 2014 along with the following additions/edits:

## ccsm3_0/wrk/example.sh

A shell script which shows the steps necessary to build and submit a CCSM3 job to Midway.

## ccsm3_0/scripts/ccsm_utils/Tools/check_machine

Line 21: Add “midway” to the list

## ccsm3_0/models/bld/Macros.Linux

This file contains the appropriate compiler flags for builsing ccsm3 models with the intlmpi/4.1+intel-12.1 and netcdf/4.2+intel-12.1 on Midway.  You will probably not need to modify this file.

## ccsm3_0/models/utils/mct/mpeu/get_zeits.c

This file was modified to avoid an issue with the now obsolete CLK_TCK constant.

```bash
Line 24: #if !defined(CLK_TCK)
Line 25: #  include <limits.h>
Line 26: #endif
```

becomes

```bash
Line 24: #define CLK_TCK CLOCKS_PER_SEC
```

## ccsm3_0/scripts/ccsm_utils/Machines/modules.linux.midway

You will need to modify this file if you intend to build ccsm3 with a different compiler, MPI library, or version of netCDF.  Here, we have set it up to work with intelmpi/4.1+intel-12.1 and netcdf/4.2+intel-12.1

## ccsm3_0/scripts/ccsm_utils/Machines/run.linux.midway

This file was adapted from run.linux.jazz and may need further modification.  It provides the skeleton script for starting a ccsm3 job.

## ccsm3_0/scripts/ccsm_utils/Machines/batch.linux.midway

This file was adapted from batch.linux.jazz and may need further modification.  It provides the skeleton submission script for running a ccsm3 job through SLURM.

## ccsm3_0/scripts/ccsm_utils/Machines/env.linux.midway

This file may need further modification to set run configuration.

This file contains environment variables including DIN_LOC_ROOT and SCRATCH.  You can also control the location of EXEROOT and RUNROOT from this file.

In this tarball, we have pointed DIN_LOC_ROOT to /project/databases/cesm which contains a copy of the CESM inputdata set which was downloaded in late-2012.  You may want to point this to a different location if you require different or more up to date inputdata.
