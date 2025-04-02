def busqueda_tabu(inicial, vecinos_func, funcion_objetivo, max_iteraciones, tamaño_tabu):
    actual = inicial
    mejor = actual
    tabu = []

    for _ in range(max_iteraciones):
        vecinos = vecinos_func(actual)
        vecinos = [n for n in vecinos if n not in tabu]

        if not vecinos:
            break

        mejor_vecino = max(vecinos, key=funcion_objetivo)

        if funcion_objetivo(mejor_vecino) > funcion_objetivo(mejor):
            mejor = mejor_vecino

        tabu.append(actual)
        if len(tabu) > tamaño_tabu:
            tabu.pop(0)

        actual = mejor_vecino

    return mejor
