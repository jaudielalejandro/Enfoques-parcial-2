# Pseudocódigo representativo, simplificado
def ao_estrella(nodo):
    if nodo.es_terminal():
        return nodo.valor

    mejor_costo = float('inf')
    mejor_opcion = None

    for opcion in nodo.opciones:
        costo = 0
        for hijo in opcion:
            costo += ao_estrella(hijo)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_opcion = opcion

    nodo.mejor_opcion = mejor_opcion
    return mejor_costo
