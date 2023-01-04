# [MITgcm](single:MITgcm)

MITgcm (the MIT General Circulation Model) can be built and run on Midway.  For more information about MITgcm and how to acquire the source code, see [http://mitgcm.org/](http://mitgcm.org/)

We recommend using the intel compiler suite with MITgcm.  The relevant modules that need to be loaded when working with MITgcm are therefore:

```bash
$ module load intelmpi/4.1+intel-12.1
$ module load netcdf/4.2+intel-12.1
```

The only Midway-specific customization you will need to use MITgcm on Midway is the following optfile for use with genmake2:

`linux_amd64_ifort+mpi_midway`

You should place this file in your instance of MITgcm’s tools/build_options/ directory and point genmake2 to it with the -of= options.

Otherwise, all of the standard MITgcm documentation can be followed verbatim.
