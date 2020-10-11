from typing import Optional
from enum import Enum

class ModelName(str, Enum):
    kwon = 'kwon'
    leem = 'leem'

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello python"}

@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"message item_id": item_id}

@app.post("/items")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item, q:Optional[str]=None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result


@app.get("/model/{name}")
async def get_model(name: ModelName):
    if name == ModelName.kwon:
        return {"model_name": name, "message": "name is kwon"}

    if name.value == "leem":
        return {"model_name": name, "message": "name is leem"}

    return {"model_name": name, "message": "name is unknown"}

