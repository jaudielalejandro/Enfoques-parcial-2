class AgenteAprendiz:
    def __init__(self):
        self.memoria = {}

    def aprender(self, percepcion, accion, resultado):
        self.memoria[(percepcion, accion)] = resultado

    def explorar(self, percepcion):
        posibles = ["accion1", "accion2"]
        return random.choice(posibles)
