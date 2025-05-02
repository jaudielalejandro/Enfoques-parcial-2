from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import Implies

A, B = symbols('A B')
reglas = And(A, Implies(A, B))  # A ∧ (A → B)

modelo = satisfiable(reglas, all_models=False)
print("Modelo que satisface:", modelo)
