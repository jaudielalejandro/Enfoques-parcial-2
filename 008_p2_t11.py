from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Datos XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

modelo = Sequential()
modelo.add(Dense(8, input_dim=2, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
modelo.fit(X, y, epochs=100, verbose=0)

print(modelo.predict(X))
