from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

app = FastAPI()

password_hash = PasswordHash.recommended()


@app.post("/login")
def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not password_hash.verify(
        password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "username": user.username
    }