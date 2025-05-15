from collections import deque

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Colas para BFS desde ambos extremos
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # Expansión desde el inicio
        camino_i = cola_inicio.popleft()
        nodo_i = camino_i[-1]

        for vecino in grafo.get(nodo_i, []):
            if vecino not in visitados_inicio:
                nuevo_camino = camino_i + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)
                if vecino in visitados_objetivo:
                    return nuevo_camino + visitados_objetivo[vecino][::-1][1:]

        # Expansión desde el objetivo
        camino_o = cola_objetivo.popleft()
        nodo_o = camino_o[-1]

        for vecino in grafo.get(nodo_o, []):
            if vecino not in visitados_objetivo:
                nuevo_camino = camino_o + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)
                if vecino in visitados_inicio:
                    return visitados_inicio[vecino] + nuevo_camino[::-1][1:]

    return None
