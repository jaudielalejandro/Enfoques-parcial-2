# Ejemplo simple: matriz de pagos para 2 jugadores
def equilibrio_nash(jugador1, jugador2):
    if jugador1 == "cooperar" and jugador2 == "cooperar":
        return (3, 3)
    elif jugador1 == "traicionar" and jugador2 == "cooperar":
        return (5, 0)
    elif jugador1 == "cooperar" and jugador2 == "traicionar":
        return (0, 5)
    else:
        return (1, 1)
