import spacy
import json
import os
from rapidfuzz import process
nlp = spacy.load("en_core_web_sm")

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR,"intents.json")

try:
    with open ("intents.json","r", encoding="utf-8") as file:
     intents = json.load(file)
except FileNotFoundError:
    print(f"Error:couldn not find {file_path}")     
    intents ={}

def process_query(query:str):
    """Process user input to extract keywords using spaCy"""
    doc = nlp(query)
    keywords= [token.lemma_ for token in doc if token.is_alpha]
    return " ".join(keywords)

def detect_intent(user_input:str):  
    """Use fuzzy matching to find the best intent from intents.json"""
    best_match = None
    best_score = 0
    for intent, patterns in intents.items():
        match, score, _=process.extractOne(user_input,patterns)
        if score > best_score:
            best_match = intent
            best_score = score
    return best_match if best_score > 70 else "unknown"  