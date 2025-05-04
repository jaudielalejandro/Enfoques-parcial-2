from sklearn.naive_bayes import GaussianNB

# Datos de ejemplo
X = [[1, 20], [2, 21], [3, 22], [4, 23]]  # características
y = [0, 0, 1, 1]                         # etiquetas

modelo = GaussianNB()
modelo.fit(X, y)

# Predicción
print(modelo.predict([[2.5, 21.5]]))
