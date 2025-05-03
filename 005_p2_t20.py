# Red semántica con relaciones
red = {
    "Canario": {"es_un": "Ave"},
    "Ave": {"puede": "volar"},
}

def razonamiento(nodo):
    if "es_un" in red.get(nodo, {}):
        padre = red[nodo]["es_un"]
        return red.get(padre, {})
    return {}

print("¿Qué puede hacer un canario?", razonamiento("Canario"))
