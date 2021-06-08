# Grover's dinner party algorithm, 
    # more people = more benefit to using QC sim

from qiskit import BasicAer
from qiskit.aqua.algorithms import Grover
from qiskit.aqua.components.oracles import LogicalExpressionOracle
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

log_expr = '((Olivia & Abe) | (Jin & Amira)) & ~(Abe & Amira)'
# ~ stands for NOT
algorithm = Grover(LogicalExpressionOracle(log_expr))

backend = BasicAer.get_backend('qasm_simulator')

result = algorithm.run(backend)

# Plot a histogram
plot_histogram(result['measurement'], title='Possible Party Combos', bar_labels = True)
plt.show()