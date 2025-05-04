# Incertidumbre es la imposibilidad de conocer un resultado con certeza
# Podemos modelarla con probabilidades.

import random

# Simulación: ¿Va a llover mañana?
def va_a_llover():
    prob_lluvia = 0.3  # 30% de probabilidad
    return random.random() < prob_lluvia
