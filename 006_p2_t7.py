# Modelo de lenguaje con bigramas
from collections import defaultdict

def entrenar_bigramas(texto):
    modelo = defaultdict(lambda: defaultdict(int))
    palabras = texto.split()
    for i in range(len(palabras)-1):
        modelo[palabras[i]][palabras[i+1]] += 1
    return modelo

def probabilidad(modelo, palabra1, palabra2):
    total = sum(modelo[palabra1].values())
    return modelo[palabra1][palabra2] / total if total > 0 else 0
