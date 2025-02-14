import spacy
nlp = spacy.load("en_core_web_sm")

def process_query(query:str):
    doc = nlp(query)
    keywords= [token.lemma_ for token in doc if token.is_alpha]
    