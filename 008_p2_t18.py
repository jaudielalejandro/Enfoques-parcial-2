# Simulación de un agente basado en reglas
base_conocimiento = {"llueve": True, "tiene_paraguas": False}
acciones = {
    "salir": lambda: not base_conocimiento["llueve"] or base_conocimiento["tiene_paraguas"]
}

print("¿Puede salir?", acciones["salir"]())
