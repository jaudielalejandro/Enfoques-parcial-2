from nltk.wsd import lesk
from nltk.corpus import wordnet
nltk.download('wordnet')

contexto = "I went to the bank to deposit money"
print("Significado probable de 'bank':", lesk(contexto.split(), "bank").definition())
