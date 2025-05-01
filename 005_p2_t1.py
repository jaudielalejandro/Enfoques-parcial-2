def profundidad_iterativa(grafo, inicio, objetivo, max_profundidad):
    # Vamos aumentando el límite poco a poco
    for limite in range(max_profundidad + 1):
        resultado = profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None
