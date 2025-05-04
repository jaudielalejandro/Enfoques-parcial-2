# Controlador PID
class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.integral = 0
        self.anterior = 0

    def actualizar(self, error, dt):
        self.integral += error * dt
        derivada = (error - self.anterior) / dt
        self.anterior = error
        return self.Kp * error + self.Ki * self.integral + self.Kd * derivada
