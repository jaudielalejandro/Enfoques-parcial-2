from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Estructura de la red
modelo = BayesianNetwork([('Lluvia', 'Tráfico'), ('HoraPico', 'Tráfico')])

# CPDs
cpd_lluvia = TabularCPD('Lluvia', 2, [[0.7], [0.3]])
cpd_hora = TabularCPD('HoraPico', 2, [[0.6], [0.4]])
cpd_trafico = TabularCPD('Tráfico', 2,
    [[0.9, 0.6, 0.7, 0.1],
     [0.1, 0.4, 0.3, 0.9]],
    evidence=['Lluvia', 'HoraPico'],
    evidence_card=[2, 2])

# Añadimos CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_hora, cpd_trafico)

# Inferencia
inferencia = VariableElimination(modelo)

# Consulta: P(Tráfico | Lluvia = Sí)
resultado = inferencia.query(variables=['Tráfico'], evidence={'Lluvia': 1})
