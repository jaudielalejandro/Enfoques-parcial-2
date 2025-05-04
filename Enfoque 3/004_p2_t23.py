import spacy
nlp = spacy.load("es_core_news_sm")

doc = nlp("El gato persigue al ratón")
for token in doc:
    print(token.text, token.dep_, token.head.text)
