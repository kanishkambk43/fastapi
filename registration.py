from fastapi import FastAPI,Depends
from pwdlib import PasswordHash
from sqlalchemy.orm import sessionmaker


Session=sessionmaker()
app=FastAPI()
User="the table of the database"

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:
        return {"message": "Username already exists"}
    password_hash=PasswordHash.recommended()

    hashed_password = password_hash.hash(password)

    user = User(
        username=username,
        password_hash=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "username": user.username
    }