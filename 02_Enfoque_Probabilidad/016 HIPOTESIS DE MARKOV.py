# P(A | B) = P(A ∩ B) / P(B)
def probabilidad_condicionada(P_AyB, P_B):
    return P_AyB / P_B

# Normalización: convierte una distribución en probabilidades válidas (que suman 1)
def normalizar(distribucion):
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}
