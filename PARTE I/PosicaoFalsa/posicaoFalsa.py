import sympy as sp

# Reading data from the file
with open('PosicaoFalsa/entrada.txt', 'r', encoding='utf-8') as file:
    a = file.readline().strip()  # Read the first line
    b = file.readline().strip()  # Read the second line
    error = file.readline().strip()  # Read the third line
    function = file.readline().strip()  # Read the fourth line

# Saving the intervals...
inf = a
sup = b

# Type conversion...
a = float(a)
b = float(b)
error = float(error)

# Transforming the function string into a symbolic expression
x = sp.symbols('x')
f = sp.sympify(function)

cont = 0
result = 0

fa = f.subs(x, a)
fb = f.subs(x, b)

while fa > error or fb > error:
    if abs(fa) < error:
        cont += 1
        result = a
        break
    if abs(fb) < error:
        cont += 1
        result = a
        break
    c = (((a * fb) - (b * fa)) / (fb - fa))
    fc = f.subs(x, c)

    if abs(fc) < error:
        fa = fc  # condição de parada
        cont += 1
        result = a
        break
    if fa * fc < 0:
        b = c
        cont += 1
    else:
        a = c
        cont += 1

fx = f.subs(x, result)

# Saving the result in the "resultado.txt" file:
with open('PosicaoFalsa/resultado.txt', 'w', encoding='utf-8') as file:
    file.write(f'================ PROBLEMA 3.6 ====================\n\n')
    file.write(f'Intervalo: [{inf}, {sup}]\n')
    file.write(f'A raiz encontrada é: {result}\n')
    file.write(f'Valor da função aplicada à raíz é: {fx}\n')
    file.write(f'Número de iterações necessárias: {cont}\n')
