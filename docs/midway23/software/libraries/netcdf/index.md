# NetCDF

To run NetCDF codes they must be compiled first, usually from a C or Fortran file

The module system has two versions of NetCDF, 3.6.3 and 4.2 (4.2 may be updated)
The reason for this is due to incompatibilities and between them - particularly
with the PGI family of compilers.

To help run fortran code simply there are several files that go along with this
help file.  Copy and run those files to test version compatibility.  A sample
file is also provided to verify proper functionality.

Example:

```bash
./pgf90-netcdf-3.6.3 simple_xy_wr.f90 output_file
./output_file
*** SUCCESS writing example file simple_xy.nc!
```
