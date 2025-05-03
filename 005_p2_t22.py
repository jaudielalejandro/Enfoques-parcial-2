def clasificar(peso):
    if peso > 50:
        return "Adulto"
    else:
        return "Niño"

print("Clasificación:", clasificar(55))
