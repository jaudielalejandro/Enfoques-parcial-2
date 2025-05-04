def profundidad_limitada(grafo, nodo, objetivo, limite):
    # Si el nodo actual es el objetivo, lo retornamos
    if nodo == objetivo:
        return [nodo]
    
    # Si llegamos al límite, no exploramos más
    if limite <= 0:
        return None

    for vecino in grafo.get(nodo, []):
        resultado = profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo] + resultado

    return None
