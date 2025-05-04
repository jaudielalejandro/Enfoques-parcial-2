from sympy import symbols, cos, sin, Eq, solve

L1, L2 = 10, 10  # Longitudes
x, y = 10, 10    # Posición deseada

t1, t2 = symbols('t1 t2')
eq1 = Eq(L1 * cos(t1) + L2 * cos(t1 + t2), x)
eq2 = Eq(L1 * sin(t1) + L2 * sin(t1 + t2), y)

sol = solve((eq1, eq2), (t1, t2))
print(sol)  # Ángulos que llevan al punto (x, y)
