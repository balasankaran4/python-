import numpy as np
A=np.array([[1,3],[2,4]])
B=np.array([3,5])
X=np.linalg.solve(A,B)
print("Solution of the LInear EquationL:\n",X)