matrix = [
    [2, -1,  0, 1],  
    [-1, 2, -1, 0], 
    [0, -1,  2, 1]   
]

n = len(matrix)

c_prime = [0.0] * (n - 1)
d_prime = [0.0] * n 
c_prime[0] = matrix[0][1] / matrix[0][0]
d_prime[0] = matrix[0][3] / matrix[0][0]
for i in range(1, n):
   
    a = matrix[i][i-1]
    b = matrix[i][i]
    
   
    m = b - a * c_prime[i-1]
    
    if i < n - 1:
        c = matrix[i][i+1]
        c_prime[i] = c / m
        

    d = matrix[i][n]
    d_prime[i] = (d - a * d_prime[i-1]) / m


x = [0.0] * n
x[n-1] = d_prime[n-1]

for i in range(n-2, -1, -1):
    x[i] = d_prime[i] - c_prime[i] * x[i+1]

print("Solution vector x:", x)
