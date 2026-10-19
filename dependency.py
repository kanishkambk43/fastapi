from fastapi import FastAPI,Depends
app =FastAPI()
def dep(name):
    return name

@app.get("/home")
def ret(data:str=Depends(dep("kanishka"))):
    return data