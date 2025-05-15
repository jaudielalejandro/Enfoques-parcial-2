# P(H|D) = P(D|H) * P(H) / P(D)
def aprendizaje_bayesiano(P_D_dado_H, P_H, P_D):
    return (P_D_dado_H * P_H) / P_D
