import random

def min_conflicts(csp, max_intentos=1000):
    asignacion = {v: random.choice(csp.dominios[v]) for v in csp.variables}

    for _ in range(max_intentos):
        conflictos = [v for v in csp.variables if not csp.es_valido({k: asignacion[k] for k in asignacion if k != v}, v, asignacion[v])]

        if not conflictos:
            return asignacion

        var = random.choice(conflictos)
        mejor_valor = min(csp.dominios[var], key=lambda val: contar_conflictos(csp, asignacion, var, val))
        asignacion[var] = mejor_valor

    return None

def contar_conflictos(csp, asignacion, var, val):
    temp_asignacion = asignacion.copy()
    temp_asignacion[var] = val
    return sum(not csp.restricciones(var, val, otro, temp_asignacion[otro]) for otro in csp.variables if otro != var)
