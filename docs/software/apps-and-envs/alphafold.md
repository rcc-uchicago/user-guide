# Alphafold

[AlphaFold](https://www.deepmind.com/research/highlighted-research/alphafold) is an artificial intelligence program developed by Google DeepMind, a subsidiary of Alphabet, which performs predictions of protein structure.

## Available modules

### AlphaFold 2

AlphaFold 2 is available as modules on Midway3 that you can check via `module avail alphafold`.

```
module avail alphafold
---------------------- /software/modulefiles----------------------------------
alphafold/2.0.0(default)  alphafold/2.2.0  alphafold/2.3.2
```

The AlphaFold source code and running scripts (e.g. `run_alphafold.py`) can be found at the Alphafold [GitHub](https://github.com/deepmind/alphafold).

The training data sets for different versions of Alphafold are accessible under `/software/alphafold-data/`, `/software/alphafold-data-2.2/` and `/software/alphafold-data-2.3/`.

### AlphaFold 3

AlphaFold 3 uses a container-based approach and requires different input arguments. See the example job script below.

## Example job scripts

Typically, Alphafold2 uses [OpenMM](https://openmm.org/), a GPU-accelerated molecular simulation package, to relax the candidate protein. OpenMM requires the CUDA toolkit to run on a GPU node.

If you want to run on a CPU-only node without the relaxation run for the candidate protein, you can run the python script `run_alphafold.py` with `--use_gpu_relax=false`.

The following example job script illustrates how to use the `alphafold/2.3.2` module on a GPU node with 2 GPUs and up to 16 CPU cores for multithreading on Midway3.

```
#!/bin/bash
#SBATCH --job-name=alphafold2
#SBATCH --account=[your-accountname]
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --time=04:00:00
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --constraint=v100
#SBATCH --mem=64G

module load alphafold/2.3.2 cuda/11.3

cd $SLURM_SUBMIT_DIR

echo "GPUs available: GPU ID $CUDA_VISIBLE_DEVICES"
echo "CPU cores: $SLURM_CPUS_PER_TASK"

DOWNLOAD_DATA_DIR=/software/alphafold-data-2.3

python run_alphafold.py \
  --data_dir=$DOWNLOAD_DATA_DIR  \
  --uniref90_database_path=$DOWNLOAD_DATA_DIR/uniref90/uniref90.fasta  \
  --mgnify_database_path=$DOWNLOAD_DATA_DIR/mgnify/mgy_clusters_2022_05.fa  \
  --bfd_database_path=$DOWNLOAD_DATA_DIR/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt  \
  --uniref30_database_path=$DOWNLOAD_DATA_DIR/uniref30/UniRef30_2021_03 \
  --pdb70_database_path=$DOWNLOAD_DATA_DIR/pdb70/pdb70  \
  --template_mmcif_dir=$DOWNLOAD_DATA_DIR/pdb_mmcif/mmcif_files  \
  --obsolete_pdbs_path=$DOWNLOAD_DATA_DIR/pdb_mmcif/obsolete.dat \
  --model_preset=monomer \
  --max_template_date=2022-1-1 \
  --db_preset=full_dbs \
  --use_gpu_relax=true \
  --output_dir=out_alphafold_2.1.1_multi-monomer \
  --fasta_paths=T1083.fasta,T1084.fasta

```

For AlphaFold 3, suppose that you have downloaded a .json file that defines the sequences for the calculation, for instance, 
[nipah_zmr.json](https://www.rbvi.ucsf.edu/chimerax/data/af3-wynton-dec2024/nipah_zmr.json) and put the downloaded json file under `/home/$USER`.

```
#!/bin/bash
#SBATCH --job-name=alphafold3
#SBATCH --account=[your-accountname]
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --time=04:00:00
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --constraint=a100
#SBATCH --mem=32G

module load apptainer

cd $SLURM_SUBMIT_DIR

mkdir -p /tmp/$USER

DOWNLOAD_DATA_DIR=/software/alphafold3.0-el8-x86_64/databases

BIND_PATHS="/software/alphafold3.0-el8-x86_64/databases,/software/alphafold3.0-el8-x86_64/params,/software/alphafold3.0-el8-x86_64/singularity,/tmp/$USER,/home/$USER,/scratch/midway3/$USER"

# Run the Singularity container `alphafold3.sif` provided under `/software/alphafold3.0-el8-x86_64` with the .json file:

singularity exec --nv \
    -B "$BIND_PATHS" \
    --env CUDA_VISIBLE_DEVICES=0,1,NVIDIA_VISIBLE_DEVICES=0,1 \
    /software/alphafold3.0-el8-x86_64/alphafold3.sif \
    python /app/alphafold/run_alphafold.py \
    --json_path=/home/$USER/nipah_zmr.json \
    --db_dir=$DOWNLOAD_DATA_DIR \
    --output_dir=/scratch/midway3/$USER/alphafold3_output \
    --model_dir=/software/alphafold3.0-el8-x86_64/params \
    --flash_attention_implementation=triton \
    --run_data_pipeline=True \
    --run_inference=True \
    --jackhmmer_n_cpu=8 \
    --nhmmer_n_cpu=8

```