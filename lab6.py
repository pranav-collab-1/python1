from cvxopt import matrix, solvers

Q = matrix([[2.0, 0.0],
            [0.0, 2.0]])

p = matrix([1.0, 1.0])

G = matrix([[-1.0, 0.0],
            [0.0, -1.0]])

h = matrix([0.0, 0.0])

A = matrix([1.0, 1.0], (1, 2))
b = matrix([1.0])

solution = solvers.qp(Q, p, G, h, A, b)

X = solution['x']

print("Optimal solution:")
print(X)
