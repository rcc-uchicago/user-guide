# Alphafold

[AlphaFold](https://www.deepmind.com/research/highlighted-research/alphafold) is an artificial intelligence program developed by DeepMind, a subsidiary of Alphabet, which performs predictions of protein structure.

## Available modules

`Alphafold2` is available as modules on Midway3 that you can check via `module avail alphafold`. The training data sets are accessible under `/software/alphafold-data/` and `/software/alphafold-data-2.2/`.

## Example job script

Typically, Alphafold2 uses OpenMM as backend which requires the CUDA toolkit to run on a GPU node. You can run the job on a CPU-only node without the relaxation run for the candidate protein (by adding `-r false` to the `run_alphafold` command).

```
#!/bin/bash
#SBATCH --job-name=alphafold2
#SBATCH --account=[your-accountname]
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --constraint=v100
#SBATCH --mem=64G

module load alphafold/2.2.0 cuda/11.3

cd $SLURM_SUBMIT_DIR

echo "GPUs available: $CUDA_VISIBLE_DEVICES"
echo "CPU cores: $SLURM_CPUS_PER_TASK"

nvidia-smi

echo "Using `which run_alphafold`"

run_alphafold -o /project/rcc/trung/test/alphafold -f /path/to/your-fasta/T1083.fasta -t 2020-07-24 -g true -u true
```