import pennylane as qml
from pennylane import numpy as pnp
from timeit import default_timer as timer

# Choose number of qubits (wires) and circuit layers
# For this setting, CPU takes ~20s, Kokkos GPU takes ~2s
wires = 20
layers = 2

# Set a seed
pnp.random.seed(42)

# Set number of runs for timing averaging
num_runs = 2

# Instantiate CPU device
# To set the number of threads used by the CPU device,
# export the OMP_NUM_THREADS environment variable.
dev = qml.device('lightning.qubit', wires=wires)

# Create QNode of device and circuit
@qml.qnode(dev)
def circuit(parameters):
    qml.StronglyEntanglingLayers(weights=parameters, wires=range(wires))
    return qml.math.hstack([qml.expval(qml.PauliZ(i)) for i in range(wires)])

# Set trainable parameters for calculating circuit Jacobian
shape = qml.StronglyEntanglingLayers.shape(n_layers=layers, n_wires=wires)
weights = pnp.random.random(size=shape)

# Run, calculate the quantum circuit Jacobian and average the timing results
timing = []
for t in range(num_runs):
    start = timer()
    jac = qml.jacobian(circuit)(weights)
    end = timer()
    timing.append(end - start)

print('Circuit measurements: \n',circuit(weights),'\n')
#print('Raw circuit: \n',qml.draw(circuit)(weights),'\n')
#print('Expanded circuit: \n',qml.draw(circuit,level='device')(weights),'\n')
print('Mean timing: ',qml.numpy.mean(timing),'\n')
