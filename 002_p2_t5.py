def iteracion_valores(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=10):
    V = {s: 0 for s in estados}

    for _ in range(iteraciones):
        nuevo_V = {}
        for s in estados:
            nuevo_V[s] = max(
                sum(p * (recompensas[s][a][s_prime] + gamma * V[s_prime])
                    for s_prime, p in transiciones[s][a].items())
                for a in acciones
            )
        V = nuevo_V
    return V
