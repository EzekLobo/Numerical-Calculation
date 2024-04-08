import numpy as np

# Reading input data
with open('FatoracaoLU/entrada.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    A = []
    for i in range(n):
        row = list(map(float, file.readline().strip().split()))
        A.append(row)
    b = list(map(float, file.readline().strip().split()))  # Read the values of the vector b
   
# LU Factorization calculation
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

# Solve linear system LU

n = len(b)
y = np.zeros(n)
x = np.zeros(n)

# Solve Ly = b
for k in range(n):
    y[k] = b[k] - sum(L[k][p] * y[p] for p in range(k))

# Solve Ux = y
for k in range(n - 1, -1, -1):
    x[k] = (y[k] - sum(U[k][p] * x[p] for p in range(k+1, n))) / U[k][k]

c = 0
# Saving the result to the file "result.txt"
with open('FatoracaoLU/result.txt', 'w', encoding='utf-8') as file:
    for line in x:
        file.write(f'x{c}: {line:.3f}\n')
        c += 1
