class Agente:
    def __init__(self):
        self.memoria = []

    def percibir(self, entorno):
        percepcion = entorno.generar_datos()
        self.memoria.append(percepcion)
        return percepcion

    def actuar(self):
        return "acción basada en memoria"

class MedioAmbiente:
    def generar_datos(self):
        return "datos del entorno"
