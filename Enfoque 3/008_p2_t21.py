# Si una acción falla, se genera un nuevo plan
try:
    ejecutar("abrir_puerta")
except:
    plan = ["buscar_llaves", "abrir_puerta"]
