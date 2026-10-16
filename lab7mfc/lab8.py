import numpy as np
import matplotlib.pyplot as plt
M = 100
dx = (1-0)/(M-1)
N = 200
dy = (2-0)/(N-1)
beta = (dx**2)/(dy**2)
X = np.linspace(0, 1, M)
Y = np.linspace(0, 2, N)
#initial soln
u = np.zeros([M, N])
u_new = u.copy()
#soln must satisfy boundary conditions
u[:,0] = 100
u[M-1,:] = 150
u[:,N-1] = 20
u[0,:] = 100
for k in range(10000):
    for j in range(1, N-1):
        for i in range(1, M-1):
            u_new[i,j] =(1/(2+2*beta))*(u[i-1,j]+beta*u[i,j-1]+u[i+1,j]+beta*u[i,j+1]-(dx**2)*(X[i]+Y[j]))
    rl= np.linalg.norm(u_new-u)/np.linalg.norm(u)
    if np.linalg.norm(u_new-u)/np.linalg.norm(u) < 10**-8:
            break
    else:
            u = u_new.copy()
            
plt.figure(figsize=(6, 5))
plt.imshow(u_new, origin='lower', cmap='jet', extent=[0, 1, 0, 2])
plt.colorbar(label='u(x, y)')
plt.title("Temperature Distribution")
plt.xlabel("x")
plt.ylabel("y")
plt.show()