# Charliecloud

[Charliecloud](https://charliecloud.io/) is a lightweight container system developed by Los Alamos National Laboratory that provides **user-defined software stacks (UDSS)** for high-performance computing (HPC). Unlike Docker or Singularity, Charliecloud uses Linux user namespaces to run completely unprivileged containers with no setuid binaries or daemons required.

## Key Features

- **Unprivileged execution** - No root or privileged operations needed
- **HPC-native** - Designed specifically for HPC environments with Slurm integration
- **Docker-compatible** - Can build and run Docker container images
- **Minimal overhead** - Fast startup with near bare-metal performance
- **Flexible storage** - Supports directory-format and SquashFS images

## Available Modules

Charliecloud is available on Midway3 via the Spack module system. First, load the Spack modules:

```bash
module load spack.modules
```

Then check available Charliecloud versions:

```bash
module avail charliecloud
```

Available versions include:
- `charliecloud/0.35-gcc-12.2.0-6ifrorq` (built with GCC)
- `charliecloud/0.35-aocc-4.1.0-65aqmle` (built with AMD AOCC)

Load the recommended GCC version:

```bash
module load charliecloud/0.35-gcc-12.2.0-6ifrorq
```

This will also load required dependencies: Python 3.11, Git, and py-requests.

## Core Commands

Charliecloud provides several key commands:

| Command | Purpose |
|---------|---------|
| `ch-image` | Build, pull, and manage container images |
| `ch-run` | Execute commands inside a container |
| `ch-convert` | Convert between image formats (e.g., Docker to SquashFS) |
| `ch-checkns` | Verify user namespace support |
| `ch-fromhost` | Inject host files into a container |
| `ch-test` | Test container functionality |

## Basic Usage

### Pulling a Docker Image

Pull an image from Docker Hub:

```bash
ch-image pull docker://ubuntu:22.04
```

This will download and cache the image in `~/.charliecloud/`.

### Running a Container

Execute a command inside a container:

```bash
ch-run ~/.charliecloud/imgs/ubuntu:22.04 -- uname -a
```

The basic syntax is:

```bash
ch-run <image_path> -- <command> [args...]
```

### Binding Directories

Mount host directories into the container using the `-b` flag:

```bash
ch-run -b $PWD:/mnt/data ~/.charliecloud/imgs/ubuntu:22.04 -- python /mnt/data/script.py
```

Multiple bind mounts are supported:

```bash
ch-run -b /path/to/input:/input \
       -b /path/to/output:/output \
       ~/.charliecloud/imgs/ubuntu:22.04 -- /run/my_pipeline.sh
```

## Example Job Script

Here is a complete SLURM job script example for running a containerized application on Midway3:

```bash
#!/bin/bash
#SBATCH --job-name=charliecloud-test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00
#SBATCH --partition=caslake
#SBATCH --account=pi-<group>

# Load Charliecloud module
module load spack.modules
module load charliecloud/0.35-gcc-12.2.0-6ifrorq

# Define paths
IMAGE_PATH=~/.charliecloud/imgs/ubuntu:22.04
INPUT_DIR=/project/$USER/my_data
OUTPUT_DIR=/scratch/$USER/results

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Run the containerized application
ch-run -b $INPUT_DIR:/data:ro \
       -b $OUTPUT_DIR:/output \
       $IMAGE_PATH -- python /process_data.py --input /data --output /output
```

## Building Custom Images

You can build custom images using a Dockerfile. Charliecloud supports Dockerfile syntax:

```dockerfile
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Install Python packages
RUN pip3 install numpy scipy matplotlib

# Set working directory
WORKDIR /workspace

# Copy your application
COPY . /workspace/

# Run your application
CMD ["python3", "my_app.py"]
```

Build the image:

```bash
ch-image build -t myapp:latest .
```

## Converting Images to SquashFS

For better performance, especially on network filesystems, convert images to SquashFS format:

```bash
ch-convert docker://ubuntu:22.04 ubuntu.sqfs
```

SquashFS images:
- Are single files that encapsulate the entire filesystem
- Have better metadata performance (important for Lustre)
- Are recommended for production use on HPC systems

## MPI Workloads

Charliecloud supports MPI applications, but requires careful configuration. Key considerations:

### MPI Launch Methods

1. **Host MPI** (Recommended): Use the host system's MPI installation
2. **Guest MPI**: MPI is installed inside the container

### Multi-node MPI Example

```bash
#!/bin/bash
#SBATCH --job-name=charliecloud-mpi
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --time=02:00:00
#SBATCH --partition=caslake

module load spack.modules
module load charliecloud/0.35-gcc-12.2.0-6ifrorq
module load openmpi

# Use host MPI with containerized application
srun ch-run --join ~/.charliecloud/imgs/myapp:latest -- /app/mpi_hello_world
```

The `--join` flag is critical for MPI - it places all ranks in the same container instance to enable shared memory communication.

!!! warning
    MPI with containers requires careful configuration. See the [official Charliecloud best practices](https://charliecloud.io/latest/best_practices.html) for detailed guidance on MPI, PMI, and fabric selection.

## Storage and Performance

### Image Storage Location

By default, Charliecloud stores images in:
- `~/.charliecloud/` for user images
- Build cache and metadata also stored here

### Temporary Directory

For large builds, you may need to redirect temporary files:

```bash
export TMPDIR=$SCRATCH/$USER/tmp
mkdir -p $TMPDIR
```

!!! note
    On Midway3, `$SCRATCH` is set to `/scratch/midway3`, so it is essential to include `$USER` in the path to ensure your files are stored in your personal scratch directory.

### Moving Charliecloud Cache to Scratch

To move the Charliecloud cache location from `~/.charliecloud/` to a scratch location permanently, use the `mvln` command from the utilities module:

```bash
module load utilities
mvln ~/.charliecloud $SCRATCH/$USER
```

## Best Practices

1. **Use SquashFS images** for better performance on shared filesystems
2. **Prefer host MPI** over guest MPI for better compatibility with cluster interconnects
3. **Bind mount strategically** - mount only the directories you need
4. **Keep images small** - use multi-stage builds and clean package caches
5. **Test locally first** - verify your container works on login nodes before submitting jobs
6. **Use `--join` for MPI** - required for multi-rank MPI jobs on the same node

## Comparison with Singularity

| Feature | Charliecloud | Singularity/Apptainer |
|---------|-------------|----------------------|
| Privilege required | Unprivileged | Setuid helper required |
| Image formats | Directory, SquashFS, Docker | SIF, Docker |
| Startup speed | Very fast | Moderate |
| Slurm integration | Native | Native |
| Complexity | Simpler | More features |

## Further Resources

- [Official Charliecloud Documentation](https://charliecloud.io/)
- [Charliecloud Tutorial](https://charliecloud.io/latest/tutorial.html)
- [Best Practices Guide](https://charliecloud.io/latest/best_practices.html)
- [Charliecloud GitHub Repository](https://github.com/hpc/charliecloud)
- [MPI Slurm Discussion](https://github.com/hpc/charliecloud/discussions/1077)
