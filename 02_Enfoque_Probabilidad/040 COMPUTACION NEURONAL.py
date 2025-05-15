# k-NN (clasificador basado en vecinos más cercanos)
from sklearn.neighbors import KNeighborsClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

modelo = KNeighborsClassifier(n_neighbors=2)
modelo.fit(X, y)

print(modelo.predict([[1.5]]))
