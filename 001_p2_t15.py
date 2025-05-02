# Ejemplo de lectura de sensor (simulada)
def sensor_ultrasonico(distancia_real_cm):
    ruido = np.random.normal(0, 0.5)
    return max(0, distancia_real_cm + ruido)

# Ejemplo de actuador (PWM)
def motor(pwm):
    if pwm > 0:
        print("Motor gira adelante")
    elif pwm < 0:
        print("Motor gira atrás")
    else:
        print("Motor detenido")
