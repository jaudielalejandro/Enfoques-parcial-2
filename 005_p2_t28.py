def evaluar_racionalidad(percepciones, acciones, resultado_esperado):
    rendimiento = sum(1 for a in acciones if a in resultado_esperado)
    return rendimiento / len(acciones)
