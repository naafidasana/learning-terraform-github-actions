from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI App"}


@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "message": "Item created succesfully"}