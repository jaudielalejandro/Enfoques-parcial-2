# Factor de certeza entre -1 (falso) y 1 (verdadero)
hechos = {"fiebre": 0.8, "tos": 0.7}

# Reglas con certeza
def diagnostico(hechos):
    if hechos["fiebre"] > 0.5 and hechos["tos"] > 0.5:
        return 0.9  # alta certeza de infección respiratoria
    return 0.3
