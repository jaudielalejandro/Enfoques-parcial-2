class Percepcion:
    def __init__(self):
        self.memoria = []

    def recibir(self, dato):
        self.memoria.append(dato)

    def secuencia(self):
        return self.memoria
