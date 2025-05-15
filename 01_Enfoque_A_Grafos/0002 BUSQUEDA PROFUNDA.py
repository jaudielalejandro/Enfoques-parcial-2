# Heurística ejemplo: distancia Manhattan (en grids)
def heuristica_manhattan(nodo_actual, nodo_objetivo):
    x1, y1 = nodo_actual
    x2, y2 = nodo_objetivo
    return abs(x1 - x2) + abs(y1 - y2)
