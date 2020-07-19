from enum import Enum

class ModelName(str, Enum):
    kwon = 'kwon'
    leem = 'leem'

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello python"}

@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"message item_id": item_id}

@app.get("/model/{name}")
async def get_model(name: ModelName):
    if name == ModelName.kwon:
        return {"model_name": name, "message": "name is kwon"}

    if name.value == "leem":
        return {"model_name": name, "message": "name is leem"}

    return {"model_name": name, "message": "name is unknown"}