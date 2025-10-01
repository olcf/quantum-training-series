import pennylane as qml

dev = qml.device("default.qubit")

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    return qml.probs()

print(circuit())
print(qml.draw(circuit)())
