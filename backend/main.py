from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router
import asyncio

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"] )

app.include_router(router)
#Home endpoint(API info)
@app.get("/")
async def home():
    return{"message":"Welcome to college chatbot API"}

