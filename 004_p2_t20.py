# Creencias de un agente
creencias = {
    "agua_hirviendo": True,
    "olla_destapada": False
}
# Razonamiento con creencias
if creencias["agua_hirviendo"] and not creencias["olla_destapada"]:
    print("Advertencia: riesgo de presión")
