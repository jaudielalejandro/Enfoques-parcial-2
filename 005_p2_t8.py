# A es independiente de B dado C si:
# P(A | B, C) = P(A | C)

# Verificación manual con ejemplos simples
P_A_dado_C = 0.6
P_A_dado_B_y_C = 0.6

def es_independiente_condicional(P1, P2):
    return abs(P1 - P2) < 1e-6  # Comparamos flotantes
