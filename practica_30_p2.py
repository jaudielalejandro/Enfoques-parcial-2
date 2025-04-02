# Un MDP define: estados, acciones, transiciones, recompensas
class MDP:
    def __init__(self, estados, acciones, transiciones, recompensas, gamma=0.9):
        self.estados = estados
        self.acciones = acciones
        self.transiciones = transiciones
        self.recompensas = recompensas
        self.gamma = gamma
