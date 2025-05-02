import numpy as np

def neurona(x, w, b):
    z = np.dot(w, x) + b  # suma ponderada + sesgo
    return z  # sin activación por ahora
