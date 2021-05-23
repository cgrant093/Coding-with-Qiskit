# from qiskit import IBMQ
# IBMQ.save_account('bd6a6d519db283bd0c78d08b151216950d3452c737cafcd2b4fb8d8a4e7ded3615f7c9cf023e45751fc03254ee97f710df3fe3c6adbf7c8862c61858e2fee53d')

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = QasmSimulator()

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
#print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit (with matplotlib)
circuit.draw(output='mpl')
#plt.show()

# Plot a histogram
plot_histogram(counts)
plt.show()