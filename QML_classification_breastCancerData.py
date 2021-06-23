# quantum machine learning: classification problem

import numpy as np
import matplotlib.pyplot as plt

from qiskit import BasicAer
from qiskit.circuit.library import ZZFeatureMap
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QSVM, SklearnSVM
from qiskit.aqua.utils import split_dataset_to_data_and_labels, map_label_to_class_name
from qiskit.ml.datasets import breast_cancer

# parameters
feature_dim = 2
training_dataset_size = 20
testing_dataset_size = 10
random_seed = 8943
shots = 10000

# setup training data
sample_total, training_input, test_input, class_labels,  = breast_cancer(
    training_size=training_dataset_size,
    test_size=testing_dataset_size,
    n=feature_dim,
    plot_data=True )
    

# setup backend, feature map, and plugged into quantum support vector machine
feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=2, entanglement='linear')
qsvm = QSVM(feature_map, training_input, test_input)

backend = BasicAer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=shots, seed_simulator=random_seed, seed_transpiler=random_seed)

result = qsvm.run(quantum_instance)

print(f'Testing success ratio: {result["testing_accuracy"]}')

# prints kernel matrix
print("kernel matrix during the trainings:")
kernel_matrix = result['kernel_matrix_training']
img = plt.imshow(np.asmatrix(kernel_matrix), interpolation='nearest', origin='upper', cmap='bone_r')
plt.show()
