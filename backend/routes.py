from fastapi import APIRouter
from backend.models import ChatRequest
from backend.responses import responses
from backend.nlp import process_query

router = APIRouter()
@router.get("/chat")
async def get_chat(query: str=""):
    """Handles GET requests (query parameters)"""
    query= query.lower().strip()
    if not query:
        return{"bot_response":"Hello! How can i assist you today?"}
    if query in responses:
        return{"bot_response":responses[query]}
    bot_response = process_query(query)
    return {"bot_response":responses[query]}

@router.post("/chat")
async def post_chat(request:ChatRequest):
    """Handles POST requests (JSON body)"""
    query = getattr(request,"user_input", "").strip().lower() 
    if not query:
          return {"bot_response":"Hello! How can i assist you today?"}
    #check predifined responses
    if query in responses:
        return{"bot_response":responses[query]}
#use nlp if no match
        bot_response =process_query(query)
        return {"bot_response":bot_responses}

