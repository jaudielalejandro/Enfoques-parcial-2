def backjumping(csp, asignacion={}, conflicto={}):
    if len(asignacion) == len(csp.variables):
        return asignacion, {}

    var = [v for v in csp.variables if v not in asignacion][0]

    for valor in csp.dominios[var]:
        conflicto[var] = set()
        consistente = True

        for asignada in asignacion:
            if not csp.restricciones(var, valor, asignada, asignacion[asignada]):
                conflicto[var].add(asignada)
                consistente = False

        if consistente:
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[var] = valor
            resultado, nuevo_conflicto = backjumping(csp, nueva_asignacion, conflicto)
            if resultado:
                return resultado, {}

            if var not in nuevo_conflicto:
                return None, nuevo_conflicto
            conflicto[var].update(nuevo_conflicto[var])
    
    return None, conflicto
