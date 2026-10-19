from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI()

# Create rate limiter
limiter = Limiter(key_func=get_remote_address)

# Add limiter to FastAPI
app.state.limiter = limiter

#tells FastAPI what to do when someone exceeds the rate limit.
app.add_exception_handler(#"This client has made too many requests."
    RateLimitExceeded,#This represents the error:"This client has made too many requests."


    _rate_limit_exceeded_handler #This is the function that handles that error.
)


@app.get("/hello")
@limiter.limit("5/minute")
def hello(request: Request):
    return {"message": "Hello"}