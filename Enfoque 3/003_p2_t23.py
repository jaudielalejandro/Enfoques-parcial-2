# Reutiliza la gramática anterior
for tree in parser.parse(tokens):
    tree.pretty_print()
