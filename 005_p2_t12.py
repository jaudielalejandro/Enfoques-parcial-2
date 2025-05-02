from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000)
mlp.fit(X, y)

print(mlp.predict(X))
