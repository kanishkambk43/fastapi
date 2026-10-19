from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/user",status_code=201)
def getuser():
    return{
        "hello it is created but we are using a modified code as 201"
    }