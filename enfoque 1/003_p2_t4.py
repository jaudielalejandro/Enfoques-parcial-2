def acondicionamiento_del_corte(csp):
    # Simplifica restricciones binarias que se pueden resolver directamente
    for var1 in csp.variables:
        for var2 in csp.variables:
            if var1 != var2:
                nuevos_dominios = []
                for val1 in csp.dominios[var1]:
                    if any(csp.restricciones(var1, val1, var2, val2) for val2 in csp.dominios[var2]):
                        nuevos_dominios.append(val1)
                csp.dominios[var1] = nuevos_dominios
