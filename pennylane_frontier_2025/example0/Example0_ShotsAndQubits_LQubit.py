import pennylane as qml

dev = qml.device("lightning.qubit", wires=2)

@qml.qnode(dev,shots=5)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    return qml.sample()

print(circuit())
print(qml.draw(circuit)())
