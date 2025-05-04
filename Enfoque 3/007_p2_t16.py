import nltk
from nltk.sem.logic import Expression

read_expr = Expression.fromstring
expr = read_expr('all x.(Gato(x) -> Animal(x))')
print(expr)
