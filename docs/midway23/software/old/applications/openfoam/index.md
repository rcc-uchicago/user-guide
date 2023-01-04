# [OpenFOAM](single:OpenFOAM)

OpenFOAM is available through the module system via **module load openfoam**

This loads `/software/openfoam-2.1-el6-x86_64/OpenFOAM/OpenFOAM-2.1.x/etc/bashrc`

This is a `bashrc` file which adds environment variables
Notable entries:

```bash
WM_PROJECT_DIR
WM_THIRD_PARTY_DIR
FOAM_APPBIN
FOAM_TUTORIALS
FOAM_RUN
```

If you use C-shell this will not work.
There is an alternate C-shell file, to load this file enter

> **source $WM_PROJECT_DIR/etc/cshrc**

The recommended starting procedure to verify proper operation is


1. Load openfoam module

    **module load openfoam**


2. Create personal OpenFOAM directory

    **mkdir -p $FOAM_RUN** (creates $HOME/OpenFOAM)


3. Copy tutorials

    **cp -ruv $FOAM_TUTORIALS $FOAM_RUN**


4. Test

```bash
cd $FOAM_RUN/tutorials/incompressible/icoFoam/cavity
blockMesh
icoFoam
paraFoam
```

**NOTE**: paraFoam is a graphical program and requires a windowing system.
See the RCC FAQ at rcc.uchicago.edu for instructions.

<!-- OpenFOAM_: http://www.openfoam.com/ -->
