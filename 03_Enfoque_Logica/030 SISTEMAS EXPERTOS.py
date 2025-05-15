# Aprendizaje No Supervisado: el modelo no tiene etiquetas
from sklearn.cluster import KMeans
import numpy as np

# Datos sin etiquetas
X = np.array([[1, 2], [2, 3], [8, 9], [9, 10]])

# Crear el modelo K-Means con 2 grupos
modelo = KMeans(n_clusters=2, random_state=42)

# Ajustar a los datos
modelo.fit(X)

# Mostrar a qué grupo pertenece cada dato
print("Etiquetas de los grupos:", modelo.labels_)
