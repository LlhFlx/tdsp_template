from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
from gensim.models import KeyedVectors



class ApiInput(BaseModel):
    words: List[str]

class ApiOutput(BaseModel):
    embedding_rep : List[List[float]]

app = FastAPI()

model = KeyedVectors.load('./models/keyed_vector_bible.kvmodel')

# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    return ApiOutput(embedding_rep=model[data.words])