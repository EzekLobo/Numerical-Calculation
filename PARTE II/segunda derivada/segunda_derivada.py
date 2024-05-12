# Implementação do método da Derivada de Segunda Ordem

from math import *

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
arquivoLer = open('input.txt', 'r')
arquivoResultado = open('output.txt', 'w')

# Função para ler os dados do arquivo de entrada
def lerArquivo():
    global arquivoLer, funcao, x

    # Lê a função e o valor de x do arquivo
    funcao = arquivoLer.readline()
    x = float(arquivoLer.readline())
 
# Função para avaliar a função fornecida em um ponto específico
def func(x):
    global funcao
    return eval(funcao)

# Função para calcular a derivada de segunda ordem
def derivadaSegunda(x):
    # Aplica a fórmula da derivada de segunda ordem
    return str((func(x + 1) - func(x)) - (func(x) - func(x - 1)))

# Função principal
def main():
    global arquivoResultado, x

    # Chama a função para ler os dados do arquivo de entrada
    lerArquivo()

    # Escreve a derivada de segunda ordem no arquivo de saída
    arquivoResultado.write("f''(x) = " + derivadaSegunda(x))
    
    # Fecha os arquivos
    arquivoLer.close()	
    arquivoResultado.close()

# Chama a função principal
main()
