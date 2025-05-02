import spacy

nlp = spacy.load("es_core_news_sm")
texto = "Pedro vive en Guadalajara y trabaja en Google."

doc = nlp(texto)
for ent in doc.ents:
    print(ent.text, ent.label_)  # Entidades nombradas
