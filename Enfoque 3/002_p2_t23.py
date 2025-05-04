import nltk
nltk.download('punkt')

texto = "El gato come ratones"
tokens = nltk.word_tokenize(texto)
print("Tokens léxicos:", tokens)
