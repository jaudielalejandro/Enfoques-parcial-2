class Vehiculo:
    def arrancar(self):
        print("Arrancando vehículo")

class Moto(Vehiculo):
    def arrancar(self):
        print("Arrancando moto")

def iniciar(v):
    v.arrancar()

iniciar(Vehiculo())
iniciar(Moto())
