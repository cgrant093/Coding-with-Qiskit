# will take state in q0 and teleport it to q2

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = QasmSimulator()

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3, 3)

# transform q0 from 0 to 1
circuit.h(0)
circuit.barrier()

# entangle q1 and q2
circuit.h(1)
circuit.cx(1,2)

# now to teleport
circuit.cx(0,1)
circuit.h(0)
circuit.barrier()

# measure q0 and q1
#   and put in classical register as c0 and c1
circuit.measure([0,1],[0,1])
circuit.barrier()

circuit.cx(1,2)
circuit.cz(0,2)

circuit.measure(2,2)

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
#print(counts)
# all results start with a '1' because that's q2/c2
# and the '1' is teleported from q0

# Draw the circuit (with matplotlib)
circuit.draw(output='mpl')
#plt.show()

# Plot a histogram
plot_histogram(counts)
plt.show()