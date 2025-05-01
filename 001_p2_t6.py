# Simplificación: red bayesiana que evoluciona en el tiempo
class RedBayesianaDinamica:
    def __init__(self, estados, transiciones):
        self.estados = estados
        self.transiciones = transiciones

    def siguiente_estado(self, estado_actual):
        from random import choices
        posibles, probs = zip(*self.transiciones[estado_actual].items())
        return choices(posibles, probs)[0]
