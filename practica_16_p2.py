import random

def algoritmo_genetico(poblacion, funcion_aptitud, seleccion, cruce, mutacion, generaciones):
    for _ in range(generaciones):
        nueva_poblacion = []

        while len(nueva_poblacion) < len(poblacion):
            padres = seleccion(poblacion, funcion_aptitud)
            hijo = cruce(*padres)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    return max(poblacion, key=funcion_aptitud)
