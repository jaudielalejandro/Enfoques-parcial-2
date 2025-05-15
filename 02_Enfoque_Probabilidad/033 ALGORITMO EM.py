from hmmlearn import hmm
import numpy as np

modelo = hmm.GaussianHMM(n_components=2)
X = np.random.randn(100, 1)  # una secuencia de observaciones
modelo.fit(X)

# Inferencia del estado oculto
estados = modelo.predict(X)
