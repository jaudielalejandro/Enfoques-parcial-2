import nltk
from nltk import CFG

# Gramática libre de contexto (CFG)
gramatica = CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'el' | 'un'
  N -> 'gato' | 'ratón'
  V -> 'come' | 'persigue'
""")

oracion = ['el', 'gato', 'persigue', 'un', 'ratón']
parser = nltk.ChartParser(gramatica)

for tree in parser.parse(oracion):
    tree.pretty_print()
