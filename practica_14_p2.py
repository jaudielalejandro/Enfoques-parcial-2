import math
import random

def temple_simulado(inicial, vecinos_func, funcion_objetivo, temperatura_inicial, enfriamiento):
    actual = inicial
    mejor = actual
    temperatura = temperatura_inicial

    while temperatura > 0.1:
        vecino = random.choice(vecinos_func(actual))
        delta = funcion_objetivo(vecino) - funcion_objetivo(actual)

        # Acepta mejor solución o peor con cierta probabilidad
        if delta > 0 or math.exp(delta / temperatura) > random.random():
            actual = vecino

        if funcion_objetivo(actual) > funcion_objetivo(mejor):
            mejor = actual

        temperatura *= enfriamiento

    return mejor
