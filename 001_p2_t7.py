import random

# Probabilidad de que un paciente tenga gripe si tiene fiebre
P_gripe = 0.2
P_fiebre_dado_gripe = 0.9
P_fiebre = 0.3

# Teorema de Bayes: P(Gripe | Fiebre)
def probabilidad_condicional():
    numerador = P_fiebre_dado_gripe * P_gripe
    denominador = P_fiebre
    return numerador / denominador
