# Librería nltk para PCFG
from nltk import Nonterminal
from nltk.grammar import PCFG
from nltk.parse.generate import generate

grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> 'el' N [0.5] | 'un' N [0.5]
    N -> 'gato' [0.6] | 'perro' [0.4]
    VP -> V NP [1.0]
    V -> 've' [0.7] | 'toca' [0.3]
""")

# Generar oraciones
for sentence in generate(grammar, n=5):
    print(' '.join(sentence))
