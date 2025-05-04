# Movimiento con incertidumbre
def mover(x, u):
    ruido = np.random.normal(0, 0.2)
    return x + u + ruido
