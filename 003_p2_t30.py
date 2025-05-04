# Agente que mantiene un modelo interno del mundo
class AgenteModelo:
    def __init__(self):
        self.estado_interno = {}

    def actualizar_estado(self, percepcion):
        self.estado_interno.update(percepcion)

    def decidir(self):
        if self.estado_interno.get("obstaculo"):
            return "esquivar"
        return "avanzar"
