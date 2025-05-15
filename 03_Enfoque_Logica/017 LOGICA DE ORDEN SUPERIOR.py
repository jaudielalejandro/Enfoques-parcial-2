# Agente tipo tabla: responde con base en una tabla predefinida de percepciones
tabla_acciones = {
    ("percepcion_1",): "accion_1",
    ("percepcion_1", "percepcion_2"): "accion_2",
    ("percepcion_1", "percepcion_2", "percepcion_3"): "accion_3"
}

def agente_tabla(percepciones):
    return tabla_acciones.get(tuple(percepciones), "accion_default")
