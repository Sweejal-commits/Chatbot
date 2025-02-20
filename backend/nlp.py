import spacy
from rapidfuzz import process,fuzz
from backend.intents import intents

nlp = spacy.load("en_core_web_sm")

def process_query(query:str):
    """Process user input to extract keywords using spaCy"""
    doc = nlp(query.lower())
    keywords= [token.lemma_ for token in doc if token.is_stop]
    return " ".join(keywords)

def detect_intent(user_input:str):  
    """Use fuzzy matching to find the best intent from intents.json"""
    processed_input = process_query(user_input)
    best_intent = None
    best_score = 0
    for intent, phrases in intents.items():
        match, score, _=process.extractOne(user_input,phrases,score = fuzz.partial_ratio)
        if score > best_score:
            best_match = intent
            best_score = score
    return best_match if best_score > 50 else "unknown"  