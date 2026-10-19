from jose import jwt 
from fastapi import FastAPI,HTTPException
from datetime import datetime,timedelta,timezone
app=FastAPI()
secret_key="kanumonu@123"
ALGO="HS256"
expires=datetime.now(timezone.utc)+timedelta(minutes=30)
payload={
    "data":"kanu",
    "exp":expires
}
JWT=jwt.encode(payload,secret_key,algorithm=ALGO)
print(JWT)
JWTdecode=jwt.decode(JWT,secret_key,algorithms=ALGO)
print(JWTdecode)

@app.post("/login")
def login(username:str,password:str):
    if username!="kanu" or password!="kanumonu":
        raise HTTPException(
            status_code=401,
            detail="not correct passoword or username"
        )
    return JWT
 