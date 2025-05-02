from sklearn.cluster import KMeans

# Datos de ejemplo
X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Predicciones de clúster
print(kmeans.labels_)
