# GROMACS

There are two different primary configuration of GROMACS:


* **gromacs-X.Y.Z** is single precision (float)


* **gromacs-plumed-X.Y.Z+<compiler module>** is double precision, compiled with the stated compiler and MPI code, with PLUMED and Reconnaissance Metadynamics

`gromacs.sbatch` demonstrates how to run a short Gromacs job (the d.dppc test
case) in parallel.  Submit to the queue by:

```bash
cd $HOME/rcchelp/software/gromacs.rcc-docs
sbatch gromacs.sbatch
# and / or
sbatch gromacs-plumed.sbatch
```

The submission scripts can be modified to suit your needs
