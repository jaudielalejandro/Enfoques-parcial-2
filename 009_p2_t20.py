# Modelo Bayesiano simple
P_lluvia = 0.3
P_nublado = 0.7
P_lluvia_dado_nublado = 0.8

# Regla de Bayes
P_nublado_dado_lluvia = (P_lluvia_dado_nublado * P_nublado) / P_lluvia
print("P(nublado|lluvia):", round(P_nublado_dado_lluvia, 2))
