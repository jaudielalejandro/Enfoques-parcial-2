class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo        # protegido
        self.__clave = "1234"      # privado

    def mostrar_saldo(self):
        return self._saldo

cuenta = Cuenta(1000)
print("Saldo:", cuenta.mostrar_saldo())
