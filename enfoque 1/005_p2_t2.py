def ascension_colinas(nodo_inicio, funcion_vecinos, heuristica):
    actual = nodo_inicio

    while True:
        vecinos = funcion_vecinos(actual)
        if not vecinos:
            break

        mejor_vecino = max(vecinos, key=lambda n: heuristica(n))
        if heuristica(mejor_vecino) <= heuristica(actual):
            break  # Ya no mejora
        actual = mejor_vecino

    return actual
