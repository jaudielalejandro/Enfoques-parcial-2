# STRIPS básico: estado, acción y resultado
estado = {"en_casa"}
accion = {
    "nombre": "ir_al_super",
    "precondiciones": {"en_casa"},
    "efectos": {"en_super"}
}

def aplicar(estado, accion):
    if accion["precondiciones"].issubset(estado):
        estado = (estado - accion["precondiciones"]) | accion["efectos"]
    return estado

print("Nuevo estado:", aplicar(estado, accion))
