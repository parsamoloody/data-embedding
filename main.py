from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

class TextInput(BaseModel):
    text: str

@app.post("/embeddings")
async def get_embeddings(input: TextInput):
    try:
        embedding = model.encode(input.text)
        embedding_list = embedding.tolist()
        return {"embeddings": embedding_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating embeddings: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Welcome to the Text Embeddings API. Use POST /embeddings to get embeddings."}