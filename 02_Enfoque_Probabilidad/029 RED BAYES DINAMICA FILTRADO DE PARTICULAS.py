# Ejemplo de red neuronal multicapa
from sklearn.neural_network import MLPClassifier

# XOR
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0, 1, 1, 0]

# Entrenamos la red
modelo = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
modelo.fit(X, y)
