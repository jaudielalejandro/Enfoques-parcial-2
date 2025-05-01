def iteracion_politicas(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=10):
    politica = {s: acciones[0] for s in estados}
    V = {s: 0 for s in estados}

    for _ in range(iteraciones):
        # Evaluación de política
        for _ in range(5):
            for s in estados:
                a = politica[s]
                V[s] = sum(p * (recompensas[s][a][s_prime] + gamma * V[s_prime])
                           for s_prime, p in transiciones[s][a].items())

        # Mejora de política
        for s in estados:
            politica[s] = max(acciones, key=lambda a: sum(
                p * (recompensas[s][a][s_prime] + gamma * V[s_prime])
                for s_prime, p in transiciones[s][a].items()))

    return politica
