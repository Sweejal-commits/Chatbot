import spacy
from rapidfuzz import fuzz
from backend.intents import intents
from backend.responses import responses

nlp = spacy.load("en_core_web_sm")

def process_query(query:str):
    """Process user input to extract keywords using spaCy"""
    doc = nlp(query.lower())
    keywords= [token.lemma_ for token in doc if token.is_stop]
    return " ".join(keywords)

def detect_intent(user_input:str):  
    """Identify the best matching intent using spaCy similarity."""
    # user_input= user_input.lower()
    # detected_intent = None
    # for intent, data in intents_responses.items():
    #     if any (pattern in user_input for pattern in data["patterns"]):
    #         detected_intent = intent
    #         break
    #     return detected_intent
    processed_input = nlp(user_input.lower())
    best_intent= "unknown"
    best_score =0.0
    for intent, phrases in intents.items():
         for phrase in phrases:
             phrase_doc = nlp(phrase.lower())
             fuzzy_score = fuzz.ratio(user_input.lower(),phrase.lower())/ 100.0
             similarity_score = processed_input.similarity(phrase_doc)
             final_score = max(fuzzy_score,similarity_score)
             if final_score > best_score and final_score >0.7
                 best_intent= intent
                 best_score= final_score
         return best_intent
    #          if similarity > best_score and similarity >0.6:
    #              best_intent= intent
    #              best_score= similarity
    # return best_intent
     
def get_response(user_input:str):
    """Get response based on identified intent"""
    intent = detect_intent(user_input)
    if intent in responses:
        response = responses[intent]
        return response if isinstance(response,str) else response[0]
    return response["unknown"]
# if __name__=="__main__":
#     user_input = input("You:")
#     print("Bot:", get_response(user_input))

 # """Identify the best matching intent using """
    # # (processed_input = process_query(user_input)
    # # best_intent = None
    # # best_score = 0
    # for intent, phrases in intents.items():
    #     for phrase in phrases:
    #         processed_phrase = process_query(phrase)
    #         if processed_phrase in processed_input or processed_input in processed_phrase:
    #             return intent
    #     return "unknown")
    #     match, score, _=process.extractOne(user_input,phrases,score = fuzz.partial_ratio)
    #     if score > best_score:
    #         best_match = intent
    #         best_score = score
    # return best_match if best_score > 50 else "unknown"