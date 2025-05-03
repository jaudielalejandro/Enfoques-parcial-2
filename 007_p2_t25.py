class Animal:
    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau"

def sonido(animal):
    print(animal.hablar())

sonido(Animal())
sonido(Perro())
