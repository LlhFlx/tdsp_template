from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


class ApiInput(BaseModel):
    word: str

class ApiOutput(BaseModel):
    embedding_rep : float

app = FastAPI()

model = np.load('./models/embeddings_bible.npz')
embeddings = {key: model[key] for key in model.files}

# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    return ApiOutput(embedding_rep=model.get(data.word))