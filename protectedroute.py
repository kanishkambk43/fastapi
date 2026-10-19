

#JWT TOKEN CREATION
def create_access_token(user_id: int):
    expires = datetime.now(timezone.utc) + timedelta(minutes=30)

    token_data = {
        "sub": str(user_id),
        "exp": expires
    }

    return jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )




#JWT TOKEN VERIFICATION
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

@app.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username
    }