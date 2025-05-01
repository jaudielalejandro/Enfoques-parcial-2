from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

modelo = BayesianNetwork([('Lluvia', 'Tráfico')])
cpd_lluvia = TabularCPD('Lluvia', 2, [[0.7], [0.3]])
cpd_trafico = TabularCPD('Tráfico', 2, [[0.8, 0.2], [0.2, 0.8]], evidence=['Lluvia'], evidence_card=[2])
modelo.add_cpds(cpd_lluvia, cpd_trafico)
