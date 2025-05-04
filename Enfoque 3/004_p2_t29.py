tabla_funcion_agente = {
    ("Percepción_1",): "Acción_1",
    ("Percepción_1", "Percepción_2"): "Acción_2",
    ("Percepción_1", "Percepción_2", "Percepción_3"): "Acción_3"
}

def programa_agente(percepciones):
    return tabla_funcion_agente.get(tuple(percepciones), "Acción por defecto")
