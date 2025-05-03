class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        return self.__saldo

cuenta = Cuenta(100)
cuenta.depositar(50)
print("Saldo:", cuenta.mostrar_saldo())
