# Usamos MiniSom (instálalo con pip install minisom)
from minisom import MiniSom

som = MiniSom(x=5, y=5, input_len=2, sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, num_iteration=100)

# El mejor nodo para una entrada:
print(som.winner([0.2, 0.7]))
