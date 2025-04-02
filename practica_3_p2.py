def dfs(grafo, inicio, objetivo):
    # Usamos una pila para seguir el camino
    pila = [[inicio]]
    visitados = set()

    while pila:
        camino = pila.pop()
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return camino

        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            pila.append(nuevo_camino)

    return None
