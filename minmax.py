import numpy as np
A = np.array([[0,7,-8,-21],[25,0,-5,0],[4,7,-8,25]])
print(A)
print(np.where(A[1,:]==0)[0])
print(np.where(A[1,:]==0)[0][0])
A[:,2]=np.where(A[:,2]<0,np.abs(A[:,2]),A[:,2])
print(A)
