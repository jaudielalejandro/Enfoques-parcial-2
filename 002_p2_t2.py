import heapq

def voraz_primero_el_mejor(grafo, inicio, objetivo, heuristica):
    frontera = [(heuristica(inicio, objetivo), [inicio])]
    visitados = set()

    while frontera:
        _, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return camino

        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            costo_estimado = heuristica(vecino, objetivo)
            heapq.heappush(frontera, (costo_estimado, nuevo_camino))

    return None
