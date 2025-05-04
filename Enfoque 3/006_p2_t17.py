hechos = {"A"}
reglas = {"A → B", "B → C"}

def encadenamiento(hechos, reglas):
    nuevos = set(hechos)
    while True:
        añadido = False
        for regla in reglas:
            antecedente, consecuente = regla.split(" → ")
            if antecedente in nuevos and consecuente not in nuevos:
                nuevos.add(consecuente)
                añadido = True
        if not añadido:
            break
    return nuevos

print(encadenamiento(hechos, reglas))
