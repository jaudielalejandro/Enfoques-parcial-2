from nltk.parse.generate import generate

gram = CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'un'
  N -> 'niño' | 'perro'
  V -> 'mira'
""")

print("Generación de frases:")
for sent in generate(gram, n=5):
    print(' '.join(sent))
