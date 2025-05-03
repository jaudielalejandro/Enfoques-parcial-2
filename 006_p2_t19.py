# Variables lingüísticas: temperatura (baja, media, alta)
# Reglas: IF temperatura is alta THEN velocidad_ventilador is rápida

# Esto se implementa mejor con `skfuzzy.control`, ejemplo completo:
from skfuzzy import control as ctrl

temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
vel = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

temp['baja'] = fuzz.trimf(temp.universe, [0, 0, 20])
temp['alta'] = fuzz.trimf(temp.universe, [20, 40, 40])
vel['lenta'] = fuzz.trimf(vel.universe, [0, 0, 50])
vel['rápida'] = fuzz.trimf(vel.universe, [50, 100, 100])

regla = ctrl.Rule(temp['alta'], vel['rápida'])

sistema = ctrl.ControlSystem([regla])
sim = ctrl.ControlSystemSimulation(sistema)
sim.input['temperatura'] = 30
sim.compute()
print("Salida difusa:", sim.output['ventilador'])
