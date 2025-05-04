# Aprendizaje por Refuerzo: se aprende a través de recompensas
import numpy as np

# Crear tabla Q vacía: 5 estados y 2 acciones posibles
Q = np.zeros((5, 2))

# Parámetros
estado = 0
accion = 1
recompensa = 10
tasa_aprendizaje = 0.1

# Actualización de Q-valor
Q[estado, accion] = Q[estado, accion] + tasa_aprendizaje * (recompensa - Q[estado, accion])

print("Tabla Q actualizada:")
print(Q)
