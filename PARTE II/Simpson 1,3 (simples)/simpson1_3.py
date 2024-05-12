from sympy import *

# Define a variável simbólica x
x = symbols('x')

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
entrada_arquivo = open('input.txt', 'r')
saida_arquivo = open('output.txt', 'w')

def ler_arquivo():
    global entrada_arquivo, funcao, a, b, n
    
    # Lê a função e os limites de integração do arquivo
    funcao = eval(entrada_arquivo.readline())
    a = float(entrada_arquivo.readline())
    b = float(entrada_arquivo.readline())
    
    # Verifica se a próxima linha não está vazia antes de tentar convertê-la para inteiro
    linha = entrada_arquivo.readline().strip()
    if linha:
        n = int(linha)
    else:
        # Se a linha estiver vazia, defina n como 1
        n = 1

def calcular_intervalos(inicio, fim, h):
    intervalos = [inicio]
    aux = inicio + h
 
    while True:
        if aux >= fim:
            break
        aux = round(aux, 2)
        intervalos.append(aux)
        aux += h
    intervalos.append(aux)
    
    return intervalos

def metodo_simpson_1_3(funcao, a, b, n):
    h = (b - a) / (2 * n)
    intervalos = calcular_intervalos(a, b, h)
    I = funcao.subs(x, a) + funcao.subs(x, b)

    for i in range(1, len(intervalos) - 1):
        valor = funcao.subs(x, intervalos[i])
        if i % 2 == 0:
            I += 2 * valor
        elif i % 2 != 0:
            I += 4 * valor
    I *= h / 3
    
    return round(I, 4)

def main():
    global saida_arquivo, funcao, a, b, n

    ler_arquivo()

    saida_arquivo.write("Valor da Integral Aproximada:\nI ~= " + str(metodo_simpson_1_3(funcao, a, b, n)))
    entrada_arquivo.close()	
    saida_arquivo.close()

main()
