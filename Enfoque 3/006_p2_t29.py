class AgenteRacional:
    def __init__(self, conocimiento_inicial):
        self.conocimiento = conocimiento_inicial

    def aprender(self, nuevo_conocimiento):
        self.conocimiento.update(nuevo_conocimiento)
