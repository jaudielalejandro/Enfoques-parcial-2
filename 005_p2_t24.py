class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Perro(Animal):
    def hablar(self):
        return "Guau"

fido = Perro("Fido")
print(fido.nombre, "dice", fido.hablar())
