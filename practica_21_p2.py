from collections import deque

def ac3(csp, dominios):
    cola = deque([(xi, xj) for xi in csp.variables for xj in csp.variables if xi != xj])

    while cola:
        xi, xj = cola.popleft()
        if revisar_arco(csp, xi, xj, dominios):
            if not dominios[xi]:
                return False
            for xk in csp.variables:
                if xk != xi and xk != xj:
                    cola.append((xk, xi))
    return True

def revisar_arco(csp, xi, xj, dominios):
    revisado = False
    for x in dominios[xi][:]:
        if not any(csp.restricciones(xi, x, xj, y) for y in dominios[xj]):
            dominios[xi].remove(x)
            revisado = True
    return revisado
