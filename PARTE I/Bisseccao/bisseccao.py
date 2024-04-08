import sympy as sp

# Reading data from the file
with open('Bisseccao/entrada.txt', 'r', encoding='utf-8') as file:
    a = file.readline().strip()  # first line 
    b = file.readline().strip()  # second line
    error = file.readline().strip()  # third line
    function = file.readline().strip()  # fourth line

# Saving the intervals...
inf = a
sup = b

# casting ...
a = float(a)
b = float(b)
error = float(error)

# create variable for the equation
x = sp.symbols('x')

# transform f into algebraic function
f = sp.sympify(function)

# counter to monitor iterations
cont = 0

if f.subs(x, a) * f.subs(x, b) >= 0:
    print("A função deve ter sinais opostos em (a) e (b).")
    SystemExit()

while (b - a) / 2.0 > error:
    c = (a + b) / 2.0
    cont += 1
    if f.subs(x, c) <= error:
        break
    elif f.subs(x, c) * f.subs(x, a) < 0:
        b = c
    else:
        a = c
    
result = (a + b) / 2.0
fx = f.subs(x, result)

# Saving the result in the txt "resultado":
with open('Bisseccao/resultado.txt', 'w', encoding='utf-8') as file:
    file.write(f'================ PROBLEMA 3.6 ====================\n\n')
    file.write(f'Intervalo: [{inf}, {sup}]\n')
    file.write(f'A raiz encontrada é: {result}\n')
    file.write(f'Valor da função aplicada à raíz é: {fx}\n')
    file.write(f'Número de iterações necessário: {cont}\n')
