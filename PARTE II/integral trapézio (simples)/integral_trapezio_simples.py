from sympy import *

# Define a variável simbólica x
x = symbols('x')

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
arquivo_entrada = open('input.txt', 'r')
arquivo_saida = open('output.txt', 'w')

# Função para ler os dados do arquivo de entrada
def ler_arquivo():
    global arquivo_entrada, funcao, limite_inferior, limite_superior
    
    # Lê a função e os limites de integração do arquivo
    funcao = eval(arquivo_entrada.readline())
    limite_inferior = float(arquivo_entrada.readline())
    limite_superior = float(arquivo_entrada.readline())

# Função para calcular a integração pelo método do trapézio simples
def trapezio_simples(limite_inferior, limite_superior, funcao):
    # Aplica a fórmula do trapézio simples
    integral = (limite_superior - limite_inferior) * ((funcao.subs(x, limite_inferior) + funcao.subs(x, limite_superior)) / 2)
    return integral

# Função principal
def main():
    global arquivo_saida, funcao, limite_inferior, limite_superior

    # Chama a função para ler os dados do arquivo de entrada
    ler_arquivo()

    # Calcula a integral pelo método do trapézio simples e escreve no arquivo de saída
    arquivo_saida.write("Valor da Integral Aproximada: \nI ~= " + str(trapezio_simples(limite_inferior, limite_superior, funcao)))
    
    # Fecha os arquivos
    arquivo_entrada.close()	
    arquivo_saida.close()

# Chama a função principal
main()
