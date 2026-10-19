from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

app = FastAPI()

SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


@app.get("/profile")
def profile(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "message": "Token is valid",
            "payload": payload
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

