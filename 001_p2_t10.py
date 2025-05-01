# Proceso estacionario simple: P(sol) = 0.7, P(lluvia) = 0.3, constante en el tiempo
def proceso_estacionario():
    return random.choices(["sol", "lluvia"], weights=[0.7, 0.3])[0]
