from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

# Dataset de ejemplo: IRIS
X, y = load_iris(return_X_y=True)
modelo = GaussianNB()
modelo.fit(X, y)

# Clasificación con probabilidades
predicciones = modelo.predict_proba(X[:2])
