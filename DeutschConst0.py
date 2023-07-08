# initialization
import numpy as np

# importing Qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble, transpile, Aer

## for display
from IPython.display import display

# import basic plot tools
from qiskit.visualization import plot_histogram

x = QuantumRegister(1,'x')
y = QuantumRegister(1,'y')
c = ClassicalRegister(1, 'c')
qc = QuantumCircuit(x,y,c)

# set qubit y to 1
qc.x(y)
qc.barrier()

# Apply H-gates for x and y
qc.h(x)
qc.h(y)

qc.barrier()

# f(x) is a constant 0 function; i.e. f(x) is always 0  
# hence, y xor f(x) is y xor 0 which yields y 

qc.barrier()

# Apply the H-gate for the top qubit x
qc.h(x)

# Measure the top qubit, i.e. q0 
qc.measure(x,c)

# Display circuit
display(qc.draw())

# use local simulator
aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(qc, aer_sim)
results = aer_sim.run(qobj,shots=1).result()
answer = results.get_counts()

print('the top qubit x: ', answer)

plot_histogram(answer)


