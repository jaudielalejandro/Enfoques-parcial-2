def funcion_agente(secuencia):
    reglas = {
        ("percepcion1",): "accion1",
        ("percepcion1", "percepcion2"): "accion2"
    }
    return reglas.get(tuple(secuencia), "accion_defecto")
