# Simulación con cadena de Markov
transiciones = {
    "sol": {"sol": 0.8, "lluvia": 0.2},
    "lluvia": {"sol": 0.4, "lluvia": 0.6}
}

def monte_carlo_markov(estado_inicial, pasos):
    estado = estado_inicial
    secuencia = [estado]
    for _ in range(pasos):
        opciones = list(transiciones[estado].keys())
        probs = list(transiciones[estado].values())
        estado = random.choices(opciones, probs)[0]
        secuencia.append(estado)
    return secuencia
