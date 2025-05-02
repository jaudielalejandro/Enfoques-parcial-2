from sympy.logic.boolalg import to_cnf

expr = Implies(A, B)  # A → B
cnf = to_cnf(expr, simplify=True)
print("Forma CNF:", cnf)
