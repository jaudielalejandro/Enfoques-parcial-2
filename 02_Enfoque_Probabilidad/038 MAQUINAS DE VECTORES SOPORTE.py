# Muestreo directo: generamos muestras desde la distribución
def muestreo_directo(distribucion, n=1000):
    eventos = list(distribucion.keys())
    probabilidades = list(distribucion.values())
    return random.choices(eventos, probabilidades, k=n)

# Muestreo por rechazo: se descartan muestras que no cumplen evidencia
def muestreo_por_rechazo(distribucion, evidencia, n=1000):
    muestras = []
    while len(muestras) < n:
        muestra = random.choices(list(distribucion.keys()), list(distribucion.values()))[0]
        if all(muestra[k] == v for k, v in evidencia.items()):
            muestras.append(muestra)
    return muestras
