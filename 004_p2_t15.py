# Espacio de configuración de un brazo 2DOF
theta1 = np.linspace(0, np.pi, 100)
theta2 = np.linspace(0, np.pi, 100)

# Todas las combinaciones posibles
espacio_config = [(t1, t2) for t1 in theta1 for t2 in theta2]
