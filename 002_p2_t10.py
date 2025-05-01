# Transiciones de una cadena de Markov
transiciones = {
    "A": {"A": 0.7, "B": 0.3},
    "B": {"A": 0.4, "B": 0.6}
}

def proceso_markov(estado_inicial, pasos):
    estado = estado_inicial
    secuencia = [estado]
    for _ in range(pasos):
        estado = random.choices(
            list(transiciones[estado].keys()),
            list(transiciones[estado].values())
        )[0]
        secuencia.append(estado)
    return secuencia
