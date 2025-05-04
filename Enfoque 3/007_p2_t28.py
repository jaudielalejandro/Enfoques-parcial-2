class AgenteAutonomo:
    def __init__(self, conocimiento_inicial=None):
        self.conocimiento = conocimiento_inicial or {}

    def actuar(self, percepcion):
        if percepcion in self.conocimiento:
            return self.conocimiento[percepcion]
        else:
            return "accion_aleatoria"
