import numpy as np

# Reading input data
with open('InversaoLU/entrada.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    A = []
    for i in range(n):
        line = list(map(float, file.readline().strip().split()))
        A.append(line)

# Calculation of LU factorization
matrix = np.array(A)
n = len(matrix)
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    L[i][i] = 1

    for j in range(i, n):
        U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
    for j in range(i+1, n):
        L[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

# Calculating the inverse matrix
identity = np.identity(n)
inverse = np.zeros((n, n))

for i in range(n):
    b = identity[:, i]
    
    # Solve the linear system LU
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = b
    for k in range(n):
        y[k] = b[k] - sum(L[k][p] * y[p] for p in range(k))

    # Solve Ux = y
    for k in range(n - 1, -1, -1):
        x[k] = (y[k] - sum(U[k][p] * x[p] for p in range(k+1, n))) / U[k][k]

    inverse[:, i] = x

# Save the inverse matrix to the file "resultado.txt"
with open('inversaoLU/resultado.txt', 'w', encoding='utf-8') as file:
    for line in inverse:
        file.write(' '.join([f'{value:.3f}' for value in line]) + '\n')
