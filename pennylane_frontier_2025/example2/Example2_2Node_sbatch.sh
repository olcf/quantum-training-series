#!/bin/sh
#SBATCH -J pennylane
#SBATCH -t 00:15:00
#SBATCH -N 2
#SBATCH -A trn043
#SBATCH --output=./log/pennylane_ex2_2nodes_%u_%j.out
#SBATCH --error=./log/err/pennylane_ex2_2nodes_%u_%j.err

module load miniforge3/23.11.0
module load PrgEnv-amd
module load rocm
module load cray-pmi
export MPICH_GPU_SUPPORT_ENABLED=1
export HSA_ENABLE_PEER_SDMA=0

source /gpfs/wolf2/olcf/trn043/proj-shared/env.sh

echo "Running Quantum Fourier Transform (QFT) on 2 Nodes: 16 GPUs"

echo ""
echo "Running 30 qubits"
srun --ntasks=16 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 30

echo ""
echo "Running 31 qubits"
srun --ntasks=16 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 31

echo ""
echo "Running 32 qubits"
srun --ntasks=16 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 32

echo ""
echo "Running 33 qubits"
srun --ntasks=16 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 33

echo ""
echo "Running 34 qubits"
srun --ntasks=16 --cpus-per-task=7 --gpus-per-task=1 --gpu-bind=closest python Example2_QFT_MPI.py 34



