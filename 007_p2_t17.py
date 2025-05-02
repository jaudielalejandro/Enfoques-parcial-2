# Resolver 2 casillas de sudoku con backtracking (simulado)
def backtracking(valores, restricciones):
    if not valores:
        return []

    for valor in valores[0]:
        if all(r(valor) for r in restricciones):
            resto = backtracking(valores[1:], restricciones)
            if resto is not None:
                return [valor] + resto
    return None
