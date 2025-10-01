#!/bin/sh
#SBATCH -J pennylane
#SBATCH -t 00:10:00
#SBATCH -N 1
#SBATCH -A trn043
#SBATCH --output=./log/pennylane_ex2_1node_%u_%j.out
#SBATCH --error=./log/err/pennylane_ex2_1node_%u_%j.err

module load miniforge3/23.11.0
module load PrgEnv-amd
module load rocm
module load cray-pmi
export MPICH_GPU_SUPPORT_ENABLED=1
export HSA_ENABLE_PEER_SDMA=0

source /gpfs/wolf2/olcf/trn043/proj-shared/env.sh

echo "Running Quantum Fourier Transform (QFT) on 1 Node"

echo ""
echo "Running on 1GPU"
srun --ntasks=1 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 30

echo ""
echo "Running on 2GPUs"
srun --ntasks=2 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 30

echo ""
echo "Running on 4GPUs"
srun --ntasks=4 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 30

echo ""
echo "Running on 8GPUs"
srun --ntasks=8 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 30


