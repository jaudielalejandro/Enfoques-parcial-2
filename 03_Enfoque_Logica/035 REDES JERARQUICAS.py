# SLAM completo requiere ROS y sensores como LIDAR.
# Simulación conceptual: se usa una nube de puntos (landmarks) + EKF o FastSLAM.
# Aquí se simula un mapa en 2D con obstáculos.

import matplotlib.pyplot as plt
mapa = np.zeros((100, 100))
mapa[20:30, 50] = 1  # obstáculo

plt.imshow(mapa, cmap="gray")
