def busqueda_online(inicio, objetivo, vecinos_func, heuristica):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = vecinos_func(actual)
        if not vecinos:
            break
        actual = min(vecinos, key=lambda n: heuristica(n, objetivo))
        camino.append(actual)

    return camino
