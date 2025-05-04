def backtracking(csp, asignacion={}):
    # Si ya asignamos todas las variables, retornamos la solución
    if len(asignacion) == len(csp.variables):
        return asignacion

    # Elegimos una variable no asignada
    var = [v for v in csp.variables if v not in asignacion][0]

    for valor in csp.dominios[var]:
        if csp.es_valido(asignacion, var, valor):
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[var] = valor
            resultado = backtracking(csp, nueva_asignacion)
            if resultado:
                return resultado

    return None
