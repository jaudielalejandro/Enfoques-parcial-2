# La función de utilidad asigna un valor numérico a un resultado
def utilidad(resultado):
    utilidades = {
        "éxito": 100,
        "fracaso": 0,
        "riesgo": 40
    }
    return utilidades.get(resultado, 0)
