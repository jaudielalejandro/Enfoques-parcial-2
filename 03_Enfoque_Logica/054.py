from sympy import Equivalent, satisfiable

# Equivalencia lógica
expr1 = A | B
expr2 = Not(Not(A) & Not(B))  # Ley de De Morgan

print("¿Son equivalentes?", Equivalent(expr1, expr2).simplify())

# ¿Es satisfacible?
print("¿Es satisfacible A ∧ ¬A?", satisfiable(And(A, Not(A))))
