#!/bin/bash
#SBATCH -A research
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --time=4-00:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=34G
#SBATCH --mail-type=END,FAIL
#SBATCH -o /scratch/arjun_sum_op.txt
#SBATCH --job-name=op_sum
module load cuda/10.1
module load cudnn/7.6-cuda-10.0
module load TensorRT/7.2.2.3
source /home2/arjunth2001/miniconda3/etc/profile.d/conda.sh
conda activate op
mkdir -p /scratch/arjunth2001
papermill  --request-save-on-cell-execute --log-output --log-level INFO --progress-bar sum.ipynb /scratch/arjunth2001/sum_out.ipynb