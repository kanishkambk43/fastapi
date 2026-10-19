from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class adress(BaseModel):
    city:str
    pincode:int
class user(BaseModel):
    name:str
    age:int
    address:adress

@app.post("/create-user")
def create(User:user):
    return {
        "message":"user got created",
        "info":User
    }