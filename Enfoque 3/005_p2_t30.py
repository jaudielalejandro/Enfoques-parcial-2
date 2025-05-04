# Agente que evalúa la utilidad de cada acción y elige la mejor
def agente_utilidad(opciones):
    utilidades = {
        "accion_a": 5,
        "accion_b": 8,
        "accion_c": 3
    }
    return max(opciones, key=lambda accion: utilidades.get(accion, 0))
