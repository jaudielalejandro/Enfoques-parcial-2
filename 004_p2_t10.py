def forward(observaciones, estados, trans, sensor, inicial):
    fwd = []
    alfa = {}
    for s in estados:
        alfa[s] = inicial[s] * sensor[s][observaciones[0]]
    fwd.append(alfa)

    for t in range(1, len(observaciones)):
        alfa = {}
        for s in estados:
            alfa[s] = sum(fwd[t-1][sp] * trans[sp][s] for sp in estados) * sensor[s][observaciones[t]]
        fwd.append(alfa)

    return fwd

def backward(observaciones, estados, trans, sensor):
    bkw = [{} for _ in range(len(observaciones))]
    for s in estados:
        bkw[-1][s] = 1

    for t in reversed(range(len(observaciones) - 1)):
        for s in estados:
            bkw[t][s] = sum(
                trans[s][sp] * sensor[sp][observaciones[t + 1]] * bkw[t + 1][sp]
                for sp in estados
            )

    return bkw
