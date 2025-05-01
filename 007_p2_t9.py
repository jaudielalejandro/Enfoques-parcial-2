def ponderacion_verosimilitud(distribucion, evidencia, n=1000):
    muestras = []
    pesos = []

    for _ in range(n):
        muestra = {}
        peso = 1
        for var in distribucion:
            if var in evidencia:
                muestra[var] = evidencia[var]
                peso *= distribucion[var].get(evidencia[var], 0)
            else:
                muestra[var] = random.choices(list(distribucion[var].keys()), list(distribucion[var].values()))[0]
        muestras.append(muestra)
        pesos.append(wpeso)

    return muestras, pesos
