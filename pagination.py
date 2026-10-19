from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "User 1"},
    {"id": 2, "name": "User 2"},
    {"id": 3, "name": "User 3"},
    {"id": 4, "name": "User 4"},
    {"id": 5, "name": "User 5"},
    {"id": 6, "name": "User 6"},
    {"id": 7, "name": "User 7"},
    {"id": 8, "name": "User 8"},
    {"id": 9, "name": "User 9"},
    {"id": 10, "name": "User 10"},
]


@app.get("/users")
def get_users(page: int = 1, limit: int = 5):

    skip = (page - 1) * limit

    return users[skip:skip + limit]