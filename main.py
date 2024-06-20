from fastapi import FastAPI, HTTPException
from classes import *
from logging_config import setup_logging

logger = setup_logging

app = FastAPI(title='Sample FastAPI Application')

# Define your API endpoints here
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    # Dummy data storage for demonstration
    database = {
        1: {"name": "Coffee", "description": "Delicious coffee", "price": 2.5, "tax": 0.1},
        2: {"name": "Tea", "description": "Green tea", "price": 1.5, "tax": 0.05}
    }
    item = database.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**item)
