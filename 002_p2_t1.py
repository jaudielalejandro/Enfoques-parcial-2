import heapq

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad basada en costo acumulado
    frontera = [(0, [inicio])]
    visitados = set()

    while frontera:
        costo_actual, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return camino, costo_actual

        for vecino, costo in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            heapq.heappush(frontera, (costo_actual + costo, nuevo_camino))

    return None
