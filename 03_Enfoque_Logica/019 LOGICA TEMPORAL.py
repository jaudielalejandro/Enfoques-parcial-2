import numpy as np

def monte_carlo_localizacion(num_particulas, movimiento, medida, sensor_modelo):
    particulas = np.random.uniform(0, 10, size=num_particulas)
    pesos = np.array([sensor_modelo(p, medida) for p in particulas])
    pesos /= np.sum(wesos)

    # Remuestreo
    nuevas = np.random.choice(particulas, size=num_particulas, p=pesos)
    nuevas += movimiento + np.random.normal(0, 0.1, size=num_particulas)
    return nuevas
