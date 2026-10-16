import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers

X = np.array([
    [0.5, 0.5],
    [1.0, 0.5],
    [-1.0, -0.5],
    [0.5, -1.0],
    [2.5, 0.5],
    [-2.5, -0.5],
    [0.5, 2.5],
    [-0.5, -2.5]
])

Y = np.array([1, 1, 1, 1, -1, -1, -1, -1])

C = 1.0
gamma = 0.5
n = len(Y)

def rbf_kernel(X1, X2):
    dist = np.sum((X1[:, None, :] - X2[None, :, :]) ** 2, axis=2)
    return np.exp(-gamma * dist)

K = rbf_kernel(X, X)
P = matrix(np.outer(Y, Y) * K, tc='d')
q = matrix(-np.ones(n), tc='d')
G = matrix(np.vstack((-np.eye(n), np.eye(n))), tc='d')
h = matrix(np.hstack((np.zeros(n), np.full(n, C))), tc='d')
A = matrix(Y.reshape(1, -1), tc='d')
b = matrix(0.0)

solvers.options['show_progress'] = False
solution = solvers.qp(P, q, G, h, A, b)

lamb = np.array(solution['x']).flatten()
indices = np.where(lamb > 1e-5)[0]

X_p = X[indices]
Y_p = Y[indices]
lamb_p = lamb[indices]

margin_indices = np.where((lamb > 1e-5) & (lamb < C - 1e-5))[0]

if len(margin_indices) > 0:
    bias_values = Y[margin_indices] - np.sum(
        (lamb * Y)[:, None] * K[:, margin_indices], axis=0
    )
    bias = np.mean(bias_values)
else:
    bias = np.mean(
        Y[indices] - np.sum(
            (lamb * Y)[:, None] * K[:, indices], axis=0
        )
    )

print("Lagrange multipliers:")
print(lamb)

print("Support vectors:")
print(X_p)

print("Bias:", bias)

def predict(X_new):
    K_new = rbf_kernel(X_new, X)
    return K_new @ (lamb * Y) + bias

x1, x2 = np.meshgrid(
    np.linspace(-3.5, 3.5, 300),
    np.linspace(-3.5, 3.5, 300)
)

grid = np.c_[x1.ravel(), x2.ravel()]
Z = predict(grid).reshape(x1.shape)

plt.contourf(x1, x2, Z, levels=[-100, 0, 100],
             alpha=0.2, colors=['red', 'blue'])
plt.contour(x1, x2, Z, levels=[-1, 0, 1],
            colors=['black', 'green', 'black'],
            linestyles=['--', '-', '--'])

plt.scatter(X[Y == 1, 0], X[Y == 1, 1],
            color='blue', label='Class +1')
plt.scatter(X[Y == -1, 0], X[Y == -1, 1],
            color='red', label='Class -1')
plt.scatter(X_p[:, 0], X_p[:, 1], s=150,
            facecolors='none', edgecolors='black',
            label='Support Vectors')

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Nonlinear Soft-Margin SVM with RBF Kernel')
plt.legend()
plt.grid(True)
plt.show()
