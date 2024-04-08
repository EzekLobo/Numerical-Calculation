# Importing the numpy library
import numpy as np

# Reading input data
expanded_matrix = np.matrix([])
error = np.array([])
with open(r"\GaussSeidel\entrada.txt", "r", encoding='utf-8') as file:
    # Retrieving precision
    error = file.readline().strip().split(" ")

    for line in file:
        # Building the expanded matrix from the input file
        # line by line from top to bottom
        row = np.matrix(line.strip().split(" "))
        expanded_matrix = np.vstack([expanded_matrix, row]) if expanded_matrix.size else row

error = np.array(error).astype(float)

# Verify if the matrix converges
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

# Solve the linear system Ax = b
def gauss_seidel_method(matrix, error_tolerance):
    matrix = matrix.astype(float)  
    rows, _ = np.shape(matrix)  

    # Verify if the matrix converges
    if not verify_matrix(matrix): 
        return None

    # Separate the matrix A and the vector b
    # create the vector x
    A_matrix = matrix[:, :-1]  
    b_vector = matrix[:, -1]  
    x_vector = np.zeros(rows)  

    # Main loop
    count = 0
    while True:
        # Make a copy of the current x vector to check for convergence
        old_x = x_vector.copy()

        for i in range(rows):
            # Update each element of the x vector using the Gauss-Seidel method
            x_vector[i] = (b_vector[i] - np.dot(A_matrix[i, :i], x_vector[:i]) - 
                           np.dot(A_matrix[i, i+1:], x_vector[i+1:])) / A_matrix[i, i]
        
        # Calculate the error as the norm of the difference between the current and the previous x
        x_error = np.linalg.norm(x_vector - old_x)  

        # Exit the loop if the error is below the tolerance
        if x_error <= error_tolerance:
            break  
        count += 1
    
    return x_vector, count 

# Print the result
result, ite = gauss_seidel_method(expanded_matrix, error)
lista = result.flatten().tolist()
with open(r"gaussSeidel\resultado.txt", "w", encoding='utf-8') as file:
    file.write(f'Número de iterações: {ite}\n')
    file.write("\n")
    for item in lista:
        file.write(f'x{lista.index(item) + 1}: {item}\n')
