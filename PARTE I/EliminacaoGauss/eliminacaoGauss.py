import numpy as np

# Reading input data
with open('EliminationGauss/entrada.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())  # Read the size of the matrix
    A = []
    for i in range(n):
        row = list(map(float, file.readline().strip().split()))
        A.append(row)
    b = list(map(float, file.readline().strip().split()))

# Gaussian elimination stage
for i in range(n):
    # Partial pivoting: row swapping if necessary
    max_row = i
    for k in range(i+1, n):
        if abs(A[k][i]) > abs(A[max_row][i]):
            max_row = k
    A[i], A[max_row] = A[max_row], A[i]
    b[i], b[max_row] = b[max_row], b[i]
        
    # Elimination of elements below the pivot
    for k in range(i+1, n):
        factor = A[k][i] / A[i][i]
        b[k] -= factor * b[i]
        for j in range(i, n):
            A[k][j] -= factor * A[i][j]

# Back substitution stage
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = b[i] / A[i][i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j] / A[i][i]

# Saving the result to txt
with open('EliminationGauss/resultado.txt', 'w', encoding='utf-8') as file:  
    for i, result in enumerate(x):
        file.write(f'x{i}: {result}\n')
