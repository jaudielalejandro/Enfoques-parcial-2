# Simulación con pydatalog o manual:
def unificar(p1, p2):
    return p1 == p2  # simple
print(unificar("padre(juan, x)", "padre(juan, pedro)"))  # No unifica por x ≠ pedro
