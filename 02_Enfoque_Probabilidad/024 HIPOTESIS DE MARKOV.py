def enumeracion(p_evidencia, distribucion_condicional):
    total = 0
    for valor in distribucion_condicional:
        prob = distribucion_condicional[valor]
        total += prob * p_evidencia(valor)
    return total
