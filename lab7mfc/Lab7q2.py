import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers

X_pos = np.array([[2, 3], [3, 3], [4, 4], [1, 2], [2, 4]])
X_neg = np.array([[6, 5], [7, 7], [8, 6], [6, 8], [7, 5], [3, 5]])

X = np.vstack((X_pos, X_neg))
Y = np.hstack((np.ones(len(X_pos)), -np.ones(len(X_neg))))

n = len(Y)
K = np.dot(X, X.T)
P = matrix(np.outer(Y, Y) * K, tc='d')
q = matrix(-np.ones(n), tc='d')
A = matrix(Y.reshape(1, -1), tc='d')
b = matrix(0.0)

solvers.options['show_progress'] = False

def solve_svm(C=None):
    if C is None:
        G = matrix(-np.eye(n), tc='d')
        h = matrix(np.zeros(n), tc='d')
    else:
        G = matrix(np.vstack((-np.eye(n), np.eye(n))), tc='d')
        h = matrix(np.hstack((np.zeros(n), np.full(n, C))), tc='d')

    solution = solvers.qp(P, q, G, h, A, b)
    lamb = np.array(solution['x']).flatten()

    indices = np.where(lamb > 1e-5)[0]
    X_p = X[indices]
    Y_p = Y[indices]
    lamb_p = lamb[indices]

    w = np.sum((lamb_p * Y_p)[:, None] * X_p, axis=0)

    if C is None:
        bias_values = Y_p - np.dot(X_p, w)
    else:
        margin_indices = np.where((lamb > 1e-5) & (lamb < C - 1e-5))[0]
        if len(margin_indices) > 0:
            bias_values = Y[margin_indices] - X[margin_indices] @ w
        else:
            bias_values = Y_p - X_p @ w

    bias = np.mean(bias_values)

    print("\nC =", C if C is not None else "Hard Margin")
    print("Weights:", w)
    print("Bias:", bias)
    print("Support Vectors:\n", X_p)

    return w, bias, indices

w_h, b_h, sv_h = solve_svm()
w_s, b_s, sv_s = solve_svm(C=1.0)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

for ax, w, bias, sv, title in [
    (axes[0], w_h, b_h, sv_h, "Hard Margin SVM"),
    (axes[1], w_s, b_s, sv_s, "Soft Margin SVM (C=1)")
]:
    ax.scatter(X_pos[:, 0], X_pos[:, 1], color='blue', label='Class +1')
    ax.scatter(X_neg[:, 0], X_neg[:, 1], color='red', label='Class -1')
    ax.scatter(X[sv, 0], X[sv, 1], s=150, facecolors='none',
               edgecolors='black', label='Support Vectors')

    x1 = np.linspace(0, 9, 200)

    if abs(w[1]) > 1e-10:
        ax.plot(x1, -(w[0] * x1 + bias) / w[1],
                'k-', label='Hyperplane')
        ax.plot(x1, -(w[0] * x1 + bias - 1) / w[1],
                'k--', label='Margins')
        ax.plot(x1, -(w[0] * x1 + bias + 1) / w[1], 'k--')

    ax.set_title(title)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
