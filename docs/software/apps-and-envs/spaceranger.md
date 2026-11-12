# Space Ranger
Space Ranger is a set of analysis pipelines that process Visium Spatial Gene Expression data with brightfield and fluorescence microscope images. See the [Space Ranger manual](https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/what-is-space-ranger) for details.

### Installation
Space Ranger comes as a precompiled binary. Use Firefox in [ThinLinc](../../connection/thinlinc/main.md) to download the [software](https://www.10xgenomics.com/support/software/space-ranger/downloads). You may create a folder called `software` in your home or project directory and extract it to that location. Replace `pi-cnetid` with your group name. For personal use, you can use the scratch storage available at `$SCRATCH/$USER`.
Set the extraction location to `/project/pi-cnetid/software` (or another location) and use the following command:

```bash
tar -xzvf spaceranger-3.0.0.tar.gz --directory /project/pi-cnetid/software
```

#### Updating PATH

After extracting the software, update the PATH as follows:

**Update PATH:**

```bash
export PATH=/project/pi-cnetid/software/spaceranger-3.0.0:$PATH
```

**Save in .bashrc:**
The command above changes `$PATH` only for the current shell. You can permanently update `PATH` by appending the following command to your `~/.bashrc` file:

```bash
echo 'export PATH=/project/pi-cnetid/software/spaceranger-3.0.0:$PATH' >> ~/.bashrc
```

These commands ensure that `spaceranger-3.0.0` is extracted to the specified location and permanently added to `PATH`, as discussed in the [Space Ranger installation guide](https://www.10xgenomics.com/support/software/space-ranger/downloads/space-ranger-installation).

Alternatively, a Space Ranger [Docker image](https://hub.docker.com/r/cumulusprod/spaceranger/tags) can be run using [Apptainer](singularity.md).


- [Tutorials](https://www.10xgenomics.com/support/software/space-ranger/latest/tutorials)

- [Job Submission Mode](https://www.10xgenomics.com/support/software/space-ranger/latest/advanced/job-submission-mode)

- [Space Ranger Cluster Mode](https://www.10xgenomics.com/support/software/space-ranger/latest/advanced/cluster-mode)
