# Reglas
reglas = [
    {"si": ["tos", "fiebre"], "entonces": "infeccion"},
    {"si": ["infeccion"], "entonces": "antibiotico"}
]

# Hechos
hechos = {"tos": True, "fiebre": True}

def inferir(hechos, reglas):
    nuevos = set()
    for r in reglas:
        if all(f in hechos for f in r["si"]):
            nuevos.add(r["entonces"])
    return nuevos

print("Inferencias:", inferir(hechos, reglas))
