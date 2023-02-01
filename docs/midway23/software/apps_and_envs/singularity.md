# Singularity

[Singularity](https://sylabs.io/) is a widely-adopted container runtime that implements a unique security model to mitigate privilege escalation risks and provides a platform to capture a complete application environment into a single file (SIF).

## Available Modules

Singularity is available on and Midway3 that you can check via `module avail singularity`. It is recommended to load the latest
version of `singularity` to have bugfixes and new features.

```
module load singularity/3.9.2
```

You can pull container Singularity and Docker container images from external sources to your spaces on the login nodes:
```
singularity pull ubuntu.sif docker://ubuntu:latest
```
and execute them on the compute nodes. You can bind and mount the paths on Midway to the containers at run time.

There are instructions to use singularity on Midway3 given [here](https://github.com/rcc-uchicago/singularity-demo).
