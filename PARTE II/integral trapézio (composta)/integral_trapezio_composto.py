from sympy import *

# Define a variável simbólica x
x = symbols('x')

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
arquivo_entrada = open('input.txt', 'r')
arquivo_saida = open('output.txt', 'w')

# Função para ler os dados do arquivo de entrada
def ler_arquivo():
    global arquivo_entrada, funcao, limite_inferior, limite_superior, num_subintervalos
    
    # Lê a função, os limites de integração e o número de subintervalos do arquivo
    funcao = eval(arquivo_entrada.readline())
    limite_inferior = float(arquivo_entrada.readline())
    limite_superior = float(arquivo_entrada.readline())
    num_subintervalos = int(arquivo_entrada.readline())

# Função para dividir o intervalo em subintervalos
def dividir_intervalo(inicio, fim, h):
    xi = [inicio]
    aux = inicio + h
    while aux < fim:
        aux = round(aux, 2)
        xi.append(aux)
        aux += h
    xi.append(aux)
    return xi

# Função para calcular a integral pelo método do trapézio múltiplo
def trapezio_multiplo(funcao, a, b, n):
    h = (b - a) / n
    xi = dividir_intervalo(a, b, h)
    tam = len(xi)
    I = funcao.subs(x, a) + funcao.subs(x, b)

    for i in range(1, tam - 1):
        I += 2 * (funcao.subs(x, xi[i]))
    I *= h / 2
    return round(I, 3)

# Função principal
def main():
    global arquivo_saida, funcao, limite_inferior, limite_superior, num_subintervalos

    # Chama a função para ler os dados do arquivo de entrada
    ler_arquivo()

    # Calcula a integral pelo método do trapézio múltiplo e escreve no arquivo de saída
    arquivo_saida.write("Valor da Integral Aproximada: \nI ~= " + str(trapezio_multiplo(funcao, limite_inferior, limite_superior, num_subintervalos)))
    
    # Fecha os arquivos
    arquivo_entrada.close()	
    arquivo_saida.close()

# Chama a função principal
main()
