# will guess a secret 6-digit number in ONE try

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# set secret number 
secretNumber = '101001'

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(6+1, 6)

# apply H gate to first 6 qubits
circuit.h([0,1,2,3,4,5])
# last gate gets X gate then H gate
circuit.x(6)
circuit.h(6)
circuit.barrier()

# build box with secret number
#   any bit that has a '1' gets a controlled X gate 
#   applied with 7th qubit (remember bits read backwards)
circuit.cx(5,6)
circuit.cx(3,6)
circuit.cx(0,6)
circuit.barrier()

# apply H gate to first 6 qubits
circuit.h([0,1,2,3,4,5])
circuit.barrier()

# now to measure
circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5])

# Use Aer's qasm_simulator
simulator = QasmSimulator()

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print(counts)
# all results start with a '1' because that's q2/c2
# and the '1' is teleported from q0

# Draw the circuit (with matplotlib)
circuit.draw(output='mpl')
plt.show()