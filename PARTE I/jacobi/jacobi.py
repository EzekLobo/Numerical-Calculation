# Importando a biblioteca numpy
import numpy as np

# Leitura dos dados de entrada
expanded_matrix = np.matrix([])
error = np.array([])
with open(r"jacobi\entrada.txt", "r", encoding='utf-8') as file:
    # Recupera a precisão
    error = file.readline().strip().split(" ")

    for line in file:
        # Constroi a matriz expandida a partir do arquivo de entrada
        # linha por linha de cima para baixo
        row = np.matrix(line.strip().split(" "))
        expanded_matrix = np.vstack([expanded_matrix, row]) if expanded_matrix.size else row

error = np.array(error).astype(float)

# Verifica se a matriz converge
def verify_matrix(matrix):
    rows,_ = np.shape(matrix)
    aux = 0
    for i in range(rows):
        for j in range(rows):
            if i != j:
                aux += abs(matrix[i, j])
                if abs(matrix[i, i]) >= aux:
                    return True
                else:
                    return False

# Resolve o sistema linear Ax = b usando o método de Jacobi
def jacobi_method(matrix, error_tolerance):
    matrix = matrix.astype(float)
    rows, _ = np.shape(matrix)
    if not verify_matrix(matrix):
        return None

    # Separa a matriz A e o vetor b
    # cria o vetor x
    A_matrix = matrix[0:, 0:-1]
    b_vector = matrix[0:, -1:]
    x_vector = np.zeros(rows)

    # Cria a matriz -B e o vetor d
    B_matrix = np.zeros((rows, rows))
    d_vector = np.zeros((rows))

    for i in range(rows):
        B_matrix[i,:] = A_matrix[i,:] / A_matrix[i, i]
        d_vector[i] = b_vector[i] / A_matrix[i, i]
        B_matrix[i, i] = 0
    B_matrix = -B_matrix

    # Calcula o vetor x
    old_x = x_vector.copy()
    x_vector = np.dot(B_matrix, x_vector) + d_vector
    x_error = np.linalg.norm(x_vector - old_x)

    # Enquanto o erro for maior que a tolerância
    count = 0
    while x_error.all() > error_tolerance:
        old_x = x_vector.copy()
        x_vector = np.dot(B_matrix, x_vector) + d_vector
        x_error = np.linalg.norm(x_vector - old_x)
        count += 1

    return x_vector, count

# Escreve a solução no arquivo de saída
x, ite = jacobi_method(expanded_matrix, error)
lista = x.flatten().tolist()
with open(r"jacobi\resultado.txt", "w", encoding='utf-8') as file:
    file.write(f'Número de iterações: {ite}\n')
    file.write("\n")
    for item in lista:
        file.write(f'x{lista.index(item) + 1}: {item}\n')
