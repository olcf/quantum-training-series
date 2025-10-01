import pennylane as qml
from catalyst import qjit
import numpy as np
import time

dev = qml.device("lightning.qubit", wires=2)
repeats = 5

# Using the `@qjit` decorator enables jit compilation mode
# Alternatively we use the AOT compilation mode below
# @qjit(autograph=True)
@qml.qnode(dev)
def circuit(x: float, loops: int):
    for i in range(0, loops):
        if x > 1.4:
            qml.RX(x, wires=0)
            qml.Hadamard(wires=0)
        else:
            qml.RY(x, wires=0)
            
        x += np.pi / 4
    return qml.expval(qml.PauliZ(0))




print("Python interpreted")
result = circuit(0.1, 10000)
print(f"Result = {result}")
start = time.time()
for _ in range(repeats):
    circuit(0.1, 10000)
end = time.time()
print(f"Time per execution: {(end - start)/repeats:.4f} seconds\n")




print("QJIT compiled")
qjitted_circuit = qjit(circuit, autograph=True)
result = qjitted_circuit(0.1, 10000)
print(f"Result = {result}")
start = time.time()
for _ in range(repeats):
    qjitted_circuit(0.1, 10000)
end = time.time()
print(f"Time per execution: {(end - start)/repeats:.4f} seconds")


