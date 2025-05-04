# Asignación de verdad que maximiza la cantidad de reglas satisfechas
def hill_climbing(proposiciones, reglas):
    import random

    estado = {p: random.choice([True, False]) for p in proposiciones}

    def puntuacion(est):
        return sum(bool(eval(r.replace("→", "<="), {}, est)) for r in reglas)

    for _ in range(100):
        vecino = estado.copy()
        cambiar = random.choice(proposiciones)
        vecino[cambiar] = not vecino[cambiar]

        if puntuacion(vecino) > puntuacion(estado):
            estado = vecino

    return estado
