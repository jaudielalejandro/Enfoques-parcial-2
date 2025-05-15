# Agente que actúa solo con la percepción actual (sin memoria ni modelo)
def agente_reactivo_simple(percepcion):
    reglas = {
        "luz": "mover_hacia_luz",
        "obstaculo": "girar"
    }
    return reglas.get(percepcion, "esperar")
