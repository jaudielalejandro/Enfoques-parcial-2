from collections import deque

def bfs(grafo, inicio, objetivo):
    # Creamos una cola para almacenar los nodos a visitar
    cola = deque([[inicio]])
    
    # Conjunto para registrar nodos visitados
    visitados = set()

    while cola:
        # Extraemos el primer camino de la cola
        camino = cola.popleft()
        nodo = camino[-1]

        # Verificamos si ya fue visitado
        if nodo in visitados:
            continue

        # Marcamos como visitado
        visitados.add(nodo)

        # Si encontramos el objetivo, retornamos el camino
        if nodo == objetivo:
            return camino

        # Agregamos caminos nuevos a la cola
        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            cola.append(nuevo_camino)

    return None
