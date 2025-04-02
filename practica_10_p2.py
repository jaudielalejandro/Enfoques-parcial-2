def busqueda_a_estrella(grafo, inicio, objetivo, heuristica):
    frontera = [(0 + heuristica(inicio, objetivo), 0, [inicio])]
    visitados = set()

    while frontera:
        f, costo_g, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return camino

        for vecino, costo in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            nuevo_costo_g = costo_g + costo
            f = nuevo_costo_g + heuristica(vecino, objetivo)
            heapq.heappush(frontera, (f, nuevo_costo_g, nuevo_camino))

    return None
