# Distribución sobre los estados del clima
distribucion = {
    "soleado": 0.5,
    "nublado": 0.3,
    "lluvioso": 0.2
}

# Elegir un estado al azar basado en su probabilidad
def muestra_distribucion(distribucion):
    eventos = list(distribucion.keys())
    probabilidades = list(distribucion.values())
    return random.choices(eventos, probabilidades)[0]
