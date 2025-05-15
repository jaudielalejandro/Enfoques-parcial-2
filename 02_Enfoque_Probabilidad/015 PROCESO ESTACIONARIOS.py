# Modelo oculto de Markov (HMM)
# Estados: 'S', 'H' (Silencio, Habla)
# Observaciones: '0', '1' (Sin sonido, sonido)

# Simplificación con probabilidades fijas
transiciones = {'S': {'S': 0.7, 'H': 0.3}, 'H': {'S': 0.4, 'H': 0.6}}
emisiones = {'S': {'0': 0.9, '1': 0.1}, 'H': {'0': 0.2, '1': 0.8}}

def viterbi(observaciones):
    V = [{}]
    estados = ['S', 'H']

    # Inicialización
    for e in estados:
        V[0][e] = {"prob": 0.5 * emisiones[e][observaciones[0]], "prev": None}

    # Recursión
    for t in range(1, len(observaciones)):
        V.append({})
        for e in estados:
            max_tr = max(V[t-1][e0]["prob"] * transiciones[e0][e] for e0 in estados)
            for e0 in estados:
                prob = V[t-1][e0]["prob"] * transiciones[e0][e] * emisiones[e][observaciones[t]]
                if prob == max_tr * emisiones[e][observaciones[t]]:
                    V[t][e] = {"prob": prob, "prev": e0}
                    break

    # Backtracking
    resultado = []
    max_final = max(V[-1], key=lambda e: V[-1][e]["prob"])
    actual = max_final
    for t in reversed(V):
        resultado.insert(0, actual)
        actual = t[actual]["prev"]
    return resultado
