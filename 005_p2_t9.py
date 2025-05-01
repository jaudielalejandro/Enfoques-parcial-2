# Supongamos que tenemos P(A, B, C) y queremos P(A, C)
P = {
    ('A1', 'B1', 'C1'): 0.1,
    ('A1', 'B2', 'C1'): 0.2,
    ('A2', 'B1', 'C1'): 0.1,
    ('A2', 'B2', 'C1'): 0.3,
}

# Eliminamos B (sumamos sobre sus valores)
def eliminar_B(P):
    resultado = {}
    for (a, b, c), valor in P.items():
        clave = (a, c)
        resultado[clave] = resultado.get(clave, 0) + valor
    return resultado
