import sympy as sp

count, result = 0, 0
# Reading data from the file
with open('Secante/entrada.txt', 'r', encoding='utf-8') as file:
    initial_x = file.readline().strip()  # Read the first line
    next_x = file.readline().strip()  # Read the second line
    error = file.readline().strip()  # Read the third line
    function = file.readline().strip()  # Read the fourth line

# Type conversion...
initial_x = float(initial_x)
next_x = float(next_x)
error = float(error)

# Saving the intervals...
inf = initial_x
sup = next_x

# Transforming the string of the function into a symbolic expression
x = sp.symbols('x')
f = sp.sympify(function)

fx0 = f.subs(x, initial_x)
fx1 = f.subs(x, next_x)

# Calculating the root
while abs(fx1) > error or abs(x2 - next_x) < error:

    if abs(fx1) < error:
        count += 1
        result = next_x
        break

    x2 = next_x - fx1 * (next_x - initial_x) / (fx1 - fx0)
    count += 1
    if abs(x2 - next_x) < error:
        count += 1
        result = x2
        break

    initial_x, next_x = next_x, x2

fx = f.subs(x, result)

# Saving the result in the "resultado.txt" file:
with open('Secante/resultado.txt', 'w', encoding='utf-8') as file:
    file.write(f'================ PROBLEMA 3.8 ====================\n\n')
    file.write(f'Intervalo: [{inf}, {sup}]\n')
    file.write(f'A raiz encontrada é: {result}\n')
    file.write(f'Valor da função aplicada à raíz é: {fx}\n')
    file.write(f'Número de iterações necessário: {count}\n')
