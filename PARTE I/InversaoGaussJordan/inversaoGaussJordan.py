import numpy as np

# Reading input data
with open('inversaoGaussJordan/entrada.txt', 'r') as file:
    n = int(file.readline().strip())
    A = []
    for i in range(n):
        line = list(map(float, file.readline().strip().split()))
        A.append(line)

# Calculation of the inverse matrix
n = len(np.array(A))
matrix = np.hstack((np.array(A), np.identity(n)))

for i in range(n):
    pivot = matrix[i, i]
        
    if pivot == 0:
        raise ValueError("The matrix is not invertible.")
        
    matrix[i, :] /= pivot

    for j in range(n):
        if i != j:
            factor = matrix[j, i]
            matrix[j, :] -= factor * matrix[i, :]

result = matrix[:, n:]

# Save the result to the file "result.txt"
with open('inversaoGaussJordan/resultado.txt', 'w') as file:
    for line in result:
        formatted_line = ' '.join([f'{value:.3f}' for value in line])
        file.write(formatted_line + '\n')
