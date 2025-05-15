# Simplificada: una red de decisión es una red bayesiana + nodo de utilidad y decisión
def red_decision(prob_llueve, utilidad_paraguas, utilidad_sin_paraguas):
    # Nodo de decisión: ¿llevar paraguas?
    decision = "sí"

    if decision == "sí":
        utilidad_esperada = utilidad_paraguas * prob_llueve + utilidad_sin_paraguas * (1 - prob_llueve)
    else:
        utilidad_esperada = utilidad_sin_paraguas * prob_llueve + utilidad_paraguas * (1 - prob_llueve)

    return utilidad_esperada
