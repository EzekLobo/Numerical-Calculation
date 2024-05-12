from sympy import symbols
from math import *

# Define a variável simbólica x usando o módulo sympy
x = symbols('x')

# Função para ler os dados do arquivo de entrada
def ler_arquivo(nome_arquivo):
    # Abre o arquivo de entrada em modo de leitura
    arquivo_leitura = open(nome_arquivo, 'r')
    # Lê a função a partir da primeira linha e a avalia usando a função eval
    funcao = eval(arquivo_leitura.readline())
    # Lê os limites de integração a e b
    a = float(arquivo_leitura.readline())
    b = float(arquivo_leitura.readline())
    # Lê o número de subintervalos para o método de Simpson 3/8
    sub_intervalos = int(arquivo_leitura.readline())
    # Fecha o arquivo após a leitura
    arquivo_leitura.close()
    # Retorna a função, os limites de integração e o número de subintervalos
    return funcao, a, b, sub_intervalos

# Função para criar os subintervalos do método de Simpson 3/8
def intervalos(inicio, fim, h):
    xi = [inicio]
    aux = inicio + h
    # Cria os subintervalos com o passo h até chegar ao limite de integração
    while(aux < fim):
        aux = round(aux, 2)
        xi.append(aux)
        aux += h
    xi.append(aux)
    # Retorna a lista de subintervalos
    return xi

# Implementação do método de Simpson 3/8
def Simpson3_8(funcao, a, b, n):
    # Calcula o tamanho do passo h
    h = (b - a) / (2*n)
    # Cria os subintervalos
    xi = intervalos(a, b, h)
    # Inicializa a integral com os valores nas extremidades dos intervalos
    I = funcao.subs(x, a) + funcao.subs(x, b)
    # Inicializa o contador para controle dos coeficientes
    count = 0
    # Percorre os subintervalos calculando a contribuição de cada um
    for i in range(1, len(xi)-1):
        aux = funcao.subs(x, xi[i])
        # Aplica os coeficientes 3 e 2 alternadamente
        if(count >= 2):
            I += 2*aux
            count = 0
        elif count < 2:
            I += 3*aux
            count += 1
    # Multiplica o resultado pelo fator (3*h)/8
    I *= (3*h)/8
    # Retorna o valor da integral aproximada, arredondado para 4 casas decimais
    return round(I, 4)

# Função principal do programa
def main():
    # Define o nome dos arquivos de entrada e saída
    nome_entrada = 'input.txt'
    nome_saida = 'output.txt'
    # Lê os dados do arquivo de entrada
    funcao, a, b, sub_inter = ler_arquivo(nome_entrada)
    # Calcula a integral usando o método de Simpson 3/8
    resultado = Simpson3_8(funcao, a, b, sub_inter)
    # Abre o arquivo de saída em modo de escrita
    arquivo_saida = open(nome_saida, 'w')
    # Escreve o resultado no arquivo de saída
    arquivo_saida.write("I(f(x)) ~= " + str(resultado))
    # Fecha o arquivo de saída
    arquivo_saida.close()

# Chama a função principal para executar o programa
main()
