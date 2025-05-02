from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, Implies

A, B = symbols('A B')

# Expresión lógica: (¬A ∨ B) ∧ (A → B)
expr = And(Or(Not(A), B), Implies(A, B))

# Evaluar para A=True, B=False
valores = {A: True, B: False}
print(expr.subs(valores))
