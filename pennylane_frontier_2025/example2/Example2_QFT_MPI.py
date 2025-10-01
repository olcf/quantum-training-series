import pennylane as qml
import numpy as np
import time
import sys

device_name = "lightning.kokkos"
mpi = True
repeats = 5

def circuit(n_qubits):
    """Mock performing a quantum Fourier transform.

    Args:
        n_qubits (int): number of wires.
    """
    dev = qml.device(device_name, wires=n_qubits, mpi=mpi)

    @qml.qnode(dev)
    def qft_circuit():
        qml.QFT(wires=range(n_qubits))
        return qml.expval(qml.PauliZ(0))
    return qft_circuit


if len(sys.argv) < 2:
    print("Usage: python test.py <n_qubits>")
    sys.exit(1)

n_qubits = int(sys.argv[1])

# warmup 
circuit(n_qubits)()


start_time = time.time()
for _ in range(repeats):
    circuit(n_qubits)()
end_time = time.time()
print(f"Time taken for {n_qubits} qubits: {(end_time - start_time)/repeats:.4f} seconds")
