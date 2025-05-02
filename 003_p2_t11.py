from sklearn.mixture import GaussianMixture
import numpy as np

X = np.random.randn(100, 2)

gmm = GaussianMixture(n_components=2)
gmm.fit(X)

# Probabilidad de pertenencia a cada componente
print(gmm.predict_proba(X[:5]))
