import skfuzzy as fuzz
import numpy as np

x = np.arange(0, 11, 1)
temperatura = fuzz.trimf(x, [0, 5, 10])  # función triangular

print(f"Grado de pertenencia a 'templado' para x=7: {fuzz.interp_membership(x, temperatura, 7)}")
