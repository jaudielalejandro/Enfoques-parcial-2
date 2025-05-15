# Estados posibles de un semáforo
estados = ["verde", "amarillo", "rojo"]
transiciones = {
    "verde": "amarillo",
    "amarillo": "rojo",
    "rojo": "verde"
}
