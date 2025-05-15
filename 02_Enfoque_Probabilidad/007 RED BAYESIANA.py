from collections import defaultdict

def entrenar_bigramas(corpus):
    modelo = defaultdict(lambda: defaultdict(int))
    palabras = corpus.split()
    for i in range(len(palabras) - 1):
        modelo[palabras[i]][palabras[i + 1]] += 1
    return modelo

def probabilidad_bigramas(modelo, palabra1, palabra2):
    total = sum(modelo[palabra1].values())
    return modelo[palabra1][palabra2] / total if total > 0 else 0

# Ejemplo
corpus = "el gato come el pescado el gato duerme"
modelo = entrenar_bigramas(corpus)
print(probabilidad_bigramas(modelo, "el", "gato"))
