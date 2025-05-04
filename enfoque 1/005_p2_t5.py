# En POMDP, el agente mantiene una creencia (probabilidad) sobre el estado
class POMDP:
    def __init__(self, estados, acciones, observaciones, transiciones, observacion_modelo, recompensas):
        self.estados = estados
        self.acciones = acciones
        self.observaciones = observaciones
        self.transiciones = transiciones
        self.observacion_modelo = observacion_modelo
        self.recompensas = recompensas

    def actualizar_creencia(self, creencia, accion, observacion):
        nueva_creencia = {}
        for s in self.estados:
            suma = sum(
                creencia[sp] * self.transiciones[sp][accion].get(s, 0) * self.observacion_modelo[s][accion].get(observacion, 0)
                for sp in self.estados
            )
            nueva_creencia[s] = suma
        # Normalizar
        total = sum(nueva_creencia.values())
        for s in nueva_creencia:
            nueva_creencia[s] /= total
        return nueva_creencia
