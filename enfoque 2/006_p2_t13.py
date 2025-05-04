traducciones = {
    "el gato": "the cat",
    "come pescado": "eats fish",
    "duerme": "sleeps"
}

def traducir(oracion):
    return ' '.join([traducciones.get(frase, frase) for frase in oracion.split(' y ')])

print(traducir("el gato y duerme"))
