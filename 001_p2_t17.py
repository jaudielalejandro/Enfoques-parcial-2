from sympy import symbols
from sympy.logic.boolalg import truth_table

A, B = symbols('A B')
expresion = A >> B

# Tabla de verdad
tt = truth_table(expresion, [A, B])
for fila in tt:
    print(fila)
