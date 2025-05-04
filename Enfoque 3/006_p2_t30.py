# Agente que aprende de la experiencia almacenando resultados
class AgenteAprendiz:
    def __init__(self):
        self.experiencias = {}

    def aprender(self, percepcion, accion, resultado):
        self.experiencias[(percepcion, accion)] = resultado

    def elegir_mejor(self, percepcion):
        acciones_posibles = [accion for (p, accion) in self.experiencias if p == percepcion]
        return acciones_posibles[0] if acciones_posibles else "accion_exploratoria"
