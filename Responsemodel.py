from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class user(BaseModel):
    name:str
    age:int
    password:str

class req(BaseModel):
    name:str
    age:int
@app.get("/student",response_model=req)
def getuser():
    return{
        "name":"kanu",
        "age":32,
        "password":"i love esports"
    }

