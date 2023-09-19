# Singularity

[Singularity](https://sylabs.io/) is a widely-adopted container runtime that implements a unique security model to mitigate privilege escalation risks and provides a platform to capture a complete application environment into a single file (SIF).

## Available Modules

Singularity is available on and Midway3 that you can check via `module avail singularity`. It is recommended to load the latest
version of `singularity` to have bugfixes and new features.

```
module load singularity/3.9.2
```

Since March 2022, Singularity has become a Linux Foundation project and renamed to [Apptainer](https://apptainer.org/).
You can load a version of Apptainer on Midway3:
```
module load apptainer/1.1.4
```
Singularity commands are highly compatible with Apptainer and vice versa.

You can pull container Singularity and Docker container images from external sources to your spaces on the login nodes:
```
singularity pull ubuntu.sif docker://ubuntu:latest
```
and execute them on the compute nodes. You can bind and mount the paths on Midway to the containers at run time.

There are instructions to use Singularity on Midway3 given [here](https://github.com/rcc-uchicago/singularity-demo).

## Example job script

Suppose that you have pulled the image from the Internet (e.g. Docker Hub) to your folder on Midway3.
In practice, you may want to bind mount the folders outside the container
(e.g. where your input data is located and where output data is to be stored) with those inside the container.
The following batch script illustrates a simple use case.

```
#!/bin/bash
#SBATCH --job-name=test-singularity
#SBATCH --nodes=1
#SBATCH --time=05:00:00
#SBATCH --account=pi-<group>
#SBATCH --partition=caslake

module load apptainer/3.9.2

singularity exec --bind /path/outside/image/:/path/inside/image/ \
                 --bind $PWD:/run/user \
                 your_image.sif your_script.py arg1 arg2

```
In this example, `/path/outside/image/` is the path in your Midway3 directory, e.g. `/project/[pi-cnetied]/your-folder/`
and `/path/inside/image/` is the path inside the container, e.g. `/tmp/`. `$PWD` is the present working directory (on Midway3)
and `/run/user` is the one present inside the container. The python script when executed inside the container will read
input from `/path/inside/image` and generate output to `/run/user/`. You can bind multiple folders.

## Known issues
As a default, Singularity uses the `/tmp` directory on the local machine (whichever node or login node you happen to be working on) to dump temporary and cache files generated during the build process. After a container is built, these are usually deleted. For containers with a large total size (more than a few GB), you may encounter an error `no space left on device`

If you see this, then it most likely means that /tmp got filled up on the machine you're using. To get around this issue, create `faketmp` and `fakecache` directories, and redirect Singularity's default temporary output to `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR`
```
export $SINGULARITY_CACHEDIR=$SCRATCH/$user/container/fakecache
export $SINGULARITY_TMPDIR=$SCRATCH/$user/container/faketmp
```
You can delete everything in the `faketmp` and `fakecache` directories after creation of your container.
