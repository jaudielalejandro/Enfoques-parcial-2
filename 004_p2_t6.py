def refuerzo_activo(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=1000):
    V = {s: 0 for s in estados}
    politica = {s: random.choice(acciones) for s in estados}

    for _ in range(iteraciones):
        for s in estados:
            valores_accion = []
            for a in acciones:
                valor = sum(p * (recompensas[s][a][s_prime] + gamma * V[s_prime])
                            for s_prime, p in transiciones[s][a].items())
                valores_accion.append((valor, a))

            mejor_valor, mejor_accion = max(valores_accion)
            V[s] = mejor_valor
            politica[s] = mejor_accion

    return politica
