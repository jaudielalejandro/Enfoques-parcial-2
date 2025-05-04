# P(Gripe | Fiebre)
P_gripe = 0.1
P_fiebre_dado_gripe = 0.8
P_fiebre = 0.3

P_gripe_dado_fiebre = regla_de_bayes(P_fiebre_dado_gripe, P_gripe, P_fiebre)
