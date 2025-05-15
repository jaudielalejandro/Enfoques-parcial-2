# Aprendizaje Supervisado: el modelo aprende de datos etiquetados
from sklearn.linear_model import LinearRegression

# Datos de entrada (X) y etiquetas (y)
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]  # Etiquetas

# Crear modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Realizar una predicción
print("Predicción para X=5:", modelo.predict([[5]]))  # Resultado esperado: 10
