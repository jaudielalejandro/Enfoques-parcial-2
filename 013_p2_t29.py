def tipo_entorno_tiempo(cambia_mientras_piensas, tiene_reloj):
    if cambia_mientras_piensas:
        return "Dinámico"
    elif tiene_reloj:
        return "Semidinámico"
    else:
        return "Estático"
