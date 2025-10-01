import pennylane as qml

dev = qml.device("lightning.qubit", wires=2)

def subcircuit(x):
    qml.RX(x,wires=0)

@qml.qnode(dev)
def circuit(x):
    for i in range(2):
        subcircuit(x)
    return qml.expval(qml.Z(wires=0))

print(circuit(0.1))
print(qml.draw(circuit)(0.1))
