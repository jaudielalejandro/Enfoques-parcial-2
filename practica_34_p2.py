def refuerzo_pasivo(politica, transiciones, recompensas, gamma=0.9, episodios=1000):
    V = {s: 0 for s in politica}

    for _ in range(episodios):
        s = random.choice(list(politica.keys()))  # Estado inicial aleatorio

        while s in politica:
            a = politica[s]
            s_prime = random.choices(list(transiciones[s][a].keys()),
                                     list(transiciones[s][a].values()))[0]
            r = recompensas[s][a][s_prime]

            # Actualización simple de valor con promedio
            V[s] = V[s] + 0.1 * (r + gamma * V.get(s_prime, 0) - V[s])
            s = s_prime

    return V
