estado_inicial = {"en_casa": True, "tiene_llaves": False}

def ir_al_coche(estado):
    if estado["en_casa"]:
        estado["en_casa"] = False
        estado["en_coche"] = True
    return estado

def tomar_llaves(estado):
    if estado.get("en_coche"):
        estado["tiene_llaves"] = True
    return estado
