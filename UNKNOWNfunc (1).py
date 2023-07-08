from qiskit import *
from qiskit.visualization import plot_histogram
import numpy as np

## for display
from IPython.display import display

def UNKNOWN(inp1,inp2):
    """An unknown function 
    
    Parameters:
        inpt1 (str): Input 1, encoded in qubit 0.
        inpt2 (str): Input 2, encoded in qubit 1.
        
    Returns:
        QuantumCircuit: Output the circuit.
        str: Output values measured from qubit 0 and qubit 1.
    """
  
    qc = QuantumCircuit(2, 2) 
    qc.reset(range(2))
    
    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)
    
    # barrier between input state and gate operation 
    qc.barrier()
    
    # add the code based on the circuit diagram in the handout


    
    
    # barrier between gate operation and measurement 
    qc.barrier()
    
    qc.measure([0,1],[0,1]) # output from qubit 0 and qubit 1 are measured
  
    #We'll run the program on a simulator
    backend = Aer.get_backend('aer_simulator')
    #Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc, shots=1, memory=True)
    out = job.result().get_memory()[0]
  
    return qc, out

## Test the function
for inp1 in ['0', '1']:
    for inp2 in ['0', '1']:
        qc, out = UNKNOWN(inp1, inp2)
        # the output string bit positions are reversed
        print('UNKNOWN func with inputs',inp1,inp2,'gives outputs',out[1],out[0])
        display(qc.draw())
        print('\n')

