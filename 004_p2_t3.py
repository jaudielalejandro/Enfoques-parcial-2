# Un CSP define variables, dominios y restricciones
class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables
        self.dominios = dominios    # Diccionario: variable -> lista de valores posibles
        self.restricciones = restricciones  # Función: var1, val1, var2, val2 -> bool

    def es_valido(self, asignacion, var_nueva, val_nuevo):
        for var, val in asignacion.items():
            if not self.restricciones(var, val, var_nueva, val_nuevo):
                return False
        return True
