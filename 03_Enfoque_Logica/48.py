class MedioAmbiente:
    def __init__(self):
        self.estado = "neutro"

    def reaccionar(self, accion):
        print(f"El medio responde a: {accion}")

class AgenteSimple:
    def __init__(self):
        self.percepciones = []

    def actuar(self, percepcion):
        self.percepciones.append(percepcion)
        return f"acción basada en {percepcion}"
