from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documentos = [
    "el gato duerme en la cama",
    "el perro ladra fuerte",
    "el gato maúlla y corre"
]

vectorizador = TfidfVectorizer()
tfidf_matrix = vectorizador.fit_transform(documentos)

# Similaridad entre documentos
sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
print(sim)  # Qué tan similar es el doc 0 a los demás
