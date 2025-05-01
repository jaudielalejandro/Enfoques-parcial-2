# P(A|B) = (P(B|A) * P(A)) / P(B)
def regla_de_bayes(P_B_dado_A, P_A, P_B):
    return (P_B_dado_A * P_A) / P_B
