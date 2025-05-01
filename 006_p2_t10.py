# Usamos filterpy para Filtro de Kalman
from filterpy.kalman import KalmanFilter

def filtro_kalman_ejemplo():
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.x = np.array([[0.], [0.]])      # estado inicial
    kf.F = np.array([[1., 1.], [0., 1.]])  # modelo de transición
    kf.H = np.array([[1., 0.]])        # modelo de observación
    kf.P *= 1000.                      # incertidumbre inicial
    kf.R = 5                           # ruido de observación
    kf.Q = 0.1                         # ruido de proceso

    mediciones = [1, 2, 3, 4]
    estimaciones = []

    for z in mediciones:
        kf.predict()
        kf.update(z)
        estimaciones.append(kf.x[0][0])

    return estimaciones
