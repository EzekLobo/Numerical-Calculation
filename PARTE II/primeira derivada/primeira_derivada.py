from math import *

# Abrir o arquivo de entrada para leitura e o arquivo de saída para escrita
file_read = open('input.txt', 'r')
file_result = open('output.txt', 'w')

# Função para ler os dados do arquivo de entrada
def read_file():
    global file_read, function, x

    # Ler a função e o valor de x do arquivo
    function = file_read.readline()
    x = float(file_read.readline())
 
# Função para avaliar a função fornecida em um ponto específico
def evaluate_function(x):
    global function
    return eval(function)

# Função para calcular a derivada de primeira ordem
def first_derivative(x):
    # Aplicar a fórmula da derivada de primeira ordem
    return str((evaluate_function(x + 1) - evaluate_function(x - 1)) / ((x + 1) - (x - 1)))

# Função principal
def main():
    global file_result, x

    # Ler os dados do arquivo de entrada
    read_file()

    # Calcular a derivada de primeira ordem e escrever no arquivo de saída
    file_result.write("Derivada de primeira ordem: \n" + first_derivative(x))
    
    # Fechar os arquivos
    file_read.close()  
    file_result.close()

# Chamar a função principal
main()
