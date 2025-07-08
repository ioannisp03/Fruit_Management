import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Fixed import path
from pydantic import BaseModel
from typing import List


# Pydantic model -> like a blueprint (Any fruit created must have a name and be str)
# Fruit inherits from the BaseModel (That's why it is a class). It validates data etc
class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: List[Fruit]


app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # JWT tokens
    allow_methods=["*"],  # specify what methods to block (POST, DELETE, Etc)
    allow_headers=["*"],  # content-type, authorization etc
)

memory_db = {"fruits": []}


@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])  # returns json


@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )  # 0.0.0.0 means run on all active IPs, app is our FastAPI app
