# Simplificado con estados S = [A, B], observaciones O = [x, y]
def filtrado(belief, trans, observacion, sensor_model):
    nueva_belief = {}
    for s in trans:
        nueva_belief[s] = sum(belief[sp] * trans[sp].get(s, 0) for sp in trans)
        nueva_belief[s] *= sensor_model[s][observacion]
    # Normalización
    total = sum(nueva_belief.values())
    for s in nueva_belief:
        nueva_belief[s] /= total
    return nueva_belief
