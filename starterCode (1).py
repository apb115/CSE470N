{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red25\green25\blue25;\red255\green255\blue255;\red25\green25\blue25;
}
{\*\expandedcolortbl;;\cssrgb\c12941\c12941\c12941;\cssrgb\c100000\c100000\c100000;\cssrgb\c12941\c12941\c12941;
}
\margl1440\margr1440\vieww15460\viewh9220\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import numpy as np\
from qiskit import QuantumCircuit, transpile\
from qiskit.providers.aer import QasmSimulator\
from qiskit.visualization import plot_histogram\
\
## for display\
from IPython.display import display\
\
# To create a Quantum Circuit with 1 qubit and 1 classical bit use\
# qc = QuantumCircuit(1,1)\
# To create a Quantum Circuit with two qubits and 2 classical bits\
# use \cf4 \cb3 \outl0\strokewidth0 qc = QuantumCircuit(2,2)\cf2 \cb3 \outl0\strokewidth0 \strokec2 \
\
# To map the quantum measurement from qubit 0 to the classical bit 0 \
# use a command like: qc.measure(0,0)\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \outl0\strokewidth0 # To map the quantum measurement from qubit 0 and1 to the classical bit 0 and 1\
# use a command like:
\fs34  
\f1\fs28 \cf0 \cb1 \kerning1\expnd0\expndtw0 qc.measure([0,1],[0,1])
\f0\fs34 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\partightenfactor0

\fs28 \cf2 \
# Draw the circuit\
display(qc.draw())\
\
\
# Use Aer's qasm_simulator\
simulator = QasmSimulator()\
\
# compile the circuit down to low-level QASM instructions\
# supported by the backend (not needed for simple circuits)\
compiled_circuit = transpile(qc, simulator)\
\
# Execute the circuit on the qasm simulator\
job = simulator.run(compiled_circuit, shots=1000)\
\
# Grab results from the job\
result = job.result()\
\
# Returns counts\
counts = result.get_counts(compiled_circuit)\
print("\\nTotal counts:",counts)\
\pard\pardeftab720\partightenfactor0

\f1 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 plot_histogram(counts)
\fs22 \

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
}