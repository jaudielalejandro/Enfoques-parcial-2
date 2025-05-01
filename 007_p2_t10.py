def filtrado_particulas(inicial, trans, sensor, observaciones, num_particulas=1000):
    particulas = [random.choice(list(inicial.keys())) for _ in range(num_particulas)]

    for obs in observaciones:
        # Predicción
        particulas = [random.choices(
            list(trans[p].keys()), list(trans[p].values()))[0] for p in particulas]

        # Ponderación
        pesos = [sensor[p][obs] for p in particulas]
        total = sum(w for w in pesos)
        pesos = [w / total for w in pesos]

        # Remuestreo
        particulas = random.choices(particulas, weights=pesos, k=num_particulas)

    # Distribución final
    from collections import Counter
    conteo = Counter(particulas)
    total = sum(conteo.values())
    return {s: c / total for s, c in conteo.items()}
