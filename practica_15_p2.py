def haz_local(iniciales, vecinos_func, funcion_objetivo, k, max_iteraciones):
    estado_actual = iniciales

    for _ in range(max_iteraciones):
        todos_vecinos = []
        for estado in estado_actual:
            todos_vecinos.extend(vecinos_func(estado))

        # Elegimos los k mejores
        estado_actual = sorted(todos_vecinos, key=funcion_objetivo, reverse=True)[:k]

    return estado_actual[0]
