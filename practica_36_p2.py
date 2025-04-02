def q_learning(estados, acciones, transiciones, recompensas, gamma=0.9, alpha=0.1, episodios=1000):
    Q = {(s, a): 0 for s in estados for a in acciones}

    for _ in range(episodios):
        s = random.choice(estados)

        while True:
            a = random.choice(acciones)
            s_prime = random.choices(list(transiciones[s][a].keys()), list(transiciones[s][a].values()))[0]
            r = recompensas[s][a][s_prime]

            max_q = max(Q[(s_prime, ap)] for ap in acciones)
            Q[(s, a)] += alpha * (r + gamma * max_q - Q[(s, a)])

            s = s_prime
            if s not in estados:
                break

    politica = {s: max(acciones, key=lambda a: Q[(s, a)]) for s in estados}
    return politica, Q
