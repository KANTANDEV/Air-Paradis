from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
# Creation de l'app FastAPI
app = FastAPI()

# Configuration de CORS
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# configuration des classes
class SentimentRequest(BaseModel):
    models: str
    text: str

@app.get("/")
def test_root():
    return {"message": "OK"}

@app.post("/analyse-sentiment")
def analyze_sentiment(request : SentimentRequest):
        if request.models == "Modèle Simple":
            return "Positif" + " " + request.text
        elif request.models == "Modèle Avancé":
            return "Négatif" + " " +  request.text
        elif request.models == "Modèle BERT":
            return "Neutre" + " " +  request.text
        