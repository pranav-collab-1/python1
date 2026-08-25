import numpy as np
A = np.array([[5,5],[5,5]])
B = np.array([[3],[4]])
x = np.array([[0],[0]])
E = 10**-8
N = 10000
k = 0
r = B - A@x
while k<N:
    p=r
    q = A@p
    alpha = (r.T@p)/(p.T@q)
    x_next = x + alpha*p
    r_next = r - alpha*q
    if np.linalg.norm(r_next)<E:
        x = x_next
        r = r_next
        k += 1
        break
    x = x_next
    r = r_next
    k+=1
print("Iterations:",k)
print(x)
