import sympy as sp

# Lendo os dados do arquivo
with open('Rahpson/entrada.txt', 'r', encoding='utf-8') as arquivo:
    x0 = arquivo.readline().strip()  # Lê a primeira linha
    erro = arquivo.readline().strip()  # Lê a segunda linha
    funcao = arquivo.readline().strip()  # Lê a terceira linha

# casting ...
x0 = float(x0)
erro = float(erro)

# salvando o inicio...
inf = x0

cont = 0

# Transformando a string da função em uma expressão simbólica
x = sp.symbols('x')
f = sp.sympify(funcao)
df = sp.diff(f, x)  # Calcula a derivada da função

x_n = x0
fx_n = f.subs(x, x_n)

while abs(fx_n) > erro:
    fx_n = f.subs(x, x_n)
    dfx_n = df.subs(x, x_n)   
    if abs(fx_n) < erro:
        resultado = x_n
        break
    x_n = x_n - fx_n / dfx_n
    cont+=1

fx = f.subs(x, resultado)

# Salvando o resultado no txt "resultado":
with open('Rahpson/resultado.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.3 ====================\n\n')
    arquivo.write(f'x0: {inf}\n')
    arquivo.write(f'A raiz encontrada é: {resultado}\n')
    arquivo.write(f'Valor da função aplicada à raíz é: {fx}\n')
    arquivo.write(f'Número de iterações necessário: {cont}\n')
