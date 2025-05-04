def busqueda_en_grafos(grafo, inicio, objetivo):
    frontera = [[inicio]]
    visitados = set()

    while frontera:
        camino = frontera.pop(0)
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return camino

        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            frontera.append(nuevo_camino)

    return None
