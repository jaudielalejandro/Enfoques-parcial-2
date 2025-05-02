from sympy.abc import x
from sympy import Predicate, Exists, ForAll

P = Predicate("EsHumano")

# "Para todo x, si x es humano, entonces es mortal"
# ∀x (EsHumano(x) → Mortal(x))
# No ejecutable directamente, pero puede representarse con frameworks como Prolog o `kanren`
