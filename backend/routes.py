from fastapi import APIRouter
from backend.models import ChatRequest
from backend.responses import responses
from backend.nlp import detect_intent,process_query
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch 

router = APIRouter()

@router.get("/chat")
async def get_chat(query: str=""):
    """Handles GET requests (query parameters)"""
    if not query:
        return{"bot_response":"Hello! How can i assist you today?"}
    if query in responses:
        return{"bot_response":responses[query]}
    intent = detect_intent(query)
    #bot_response = process_query(query)
    return {"bot_response":responses.get(intent,"I'm not sure how to respond.")}
@router.post("/chat")
async def post_chat(request:ChatRequest):
    """Handles POST requests (JSON body)"""
    user_input = request.get("message","").strip().lower() 
    if not user_input:
        return {"bot_response":"Hello!How can i assist you"}
    response_text = process_query(user_input)
    return{"bot_response":response_text}
#     query = getattr(request,"user_input", "").strip().lower() 
#     if not query:
#           return {"bot_response":"Hello! How can i assist you today?"}
#     #check predifined responses
#     if query in responses:
#         return{"bot_response":responses[query]}
# #use nlp intent dectetion
#     intent = detect_intent(query)
#     # bot_response = detect_intent(query)
#     return {"bot_response":responses.get(intent,"I'm not sure how to respond.")}


