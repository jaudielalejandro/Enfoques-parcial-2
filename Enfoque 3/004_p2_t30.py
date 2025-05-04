# Agente que elige acciones para alcanzar un objetivo
class AgenteObjetivo:
    def __init__(self, objetivo):
        self.objetivo = objetivo

    def decidir(self, estado_actual):
        if estado_actual != self.objetivo:
            return "buscar_cambio"
        return "mantener"
