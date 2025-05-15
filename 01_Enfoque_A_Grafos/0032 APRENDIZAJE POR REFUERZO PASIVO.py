def forward_checking(csp, asignacion, dominios):
    if len(asignacion) == len(csp.variables):
        return asignacion

    var = [v for v in csp.variables if v not in asignacion][0]

    for valor in dominios[var]:
        if csp.es_valido(asignacion, var, valor):
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[var] = valor

            nuevo_dominio = {v: list(d) for v, d in dominios.items()}
            for vecino in csp.variables:
                if vecino != var and vecino not in asignacion:
                    nuevo_dominio[vecino] = [v for v in nuevo_dominio[vecino]
                                              if csp.es_valido(nueva_asignacion, vecino, v)]

                    if not nuevo_dominio[vecino]:  # Se quedó sin opciones
                        break
            else:
                resultado = forward_checking(csp, nueva_asignacion, nuevo_dominio)
                if resultado:
                    return resultado

    return None
