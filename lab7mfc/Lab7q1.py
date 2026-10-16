import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers

X_pos = np.array([[2, 3], [3, 3], [4, 4], [1, 2], [2, 4]])
X_neg = np.array([[6, 5], [7, 7], [8, 6], [6, 8], [7, 5]])

X = np.vstack((X_pos, X_neg))
Y = np.hstack((np.ones(len(X_pos)), -np.ones(len(X_neg))))

n = len(Y)

K = np.dot(X, X.T)
P = matrix(np.outer(Y, Y) * K, tc='d')
q = matrix(-np.ones(n), tc='d')
G = matrix(-np.eye(n), tc='d')
h = matrix(np.zeros(n), tc='d')
A = matrix(Y.reshape(1, -1), tc='d')
b = matrix(0.0)

solvers.options['show_progress'] = False
solution = solvers.qp(P, q, G, h, A, b)

lamb = np.array(solution['x']).flatten()
indices = np.where(lamb > 1e-5)[0]

X_p = X[indices]
Y_p = Y[indices]
lamb_p = lamb[indices]

w = np.sum((lamb_p * Y_p)[:, None] * X_p, axis=0)

bias_values = Y_p - np.dot(X_p, w)
bias = np.mean(bias_values)

print("Lagrange multipliers:")
print(lamb)

print("Support vectors:")
print(X_p)

print("Weights:", w)
print("Bias:", bias)

plt.scatter(X_pos[:, 0], X_pos[:, 1], color='blue', label='Positive Class')
plt.scatter(X_neg[:, 0], X_neg[:, 1], color='red', label='Negative Class')
plt.scatter(X_p[:, 0], X_p[:, 1], s=150, facecolors='none',
            edgecolors='black', label='Support Vectors')

x1 = np.linspace(0, 9, 200)

if abs(w[1]) > 1e-10:
    decision = -(w[0] * x1 + bias) / w[1]
    margin1 = -(w[0] * x1 + bias - 1) / w[1]
    margin2 = -(w[0] * x1 + bias + 1) / w[1]

    plt.plot(x1, decision, 'k-', label='Hyperplane')
    plt.plot(x1, margin1, 'k--', label='Margins')
    plt.plot(x1, margin2, 'k--')

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Linear SVM - Hard Margin')
plt.legend()
plt.grid(True)
plt.show()
