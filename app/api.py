# API voor users met passwoorden opgeslagen in db + hashing?

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Brecht Voets 2CCS01's API🔥",description="Welcome to my cool user API, where I made a replica of a real website login page that stores data in a database, hashed ofcourse!")

class db_User(BaseModel):
    first_name: str
    last_name: str
    registration_date: datetime
    password: str
    ID: int


class User(BaseModel):
    first_name: str
    last_name: str
    password: str
    registration_date: datetime | None = None  # User zou dit nu nog kunnen invullen, zou niet mogen
    ID: int | None = None  # zelfde hier


class Secure_User(BaseModel):
    first_name: str
    last_name: str
    registration_date: datetime
    ID: int


user_brecht = {
    "first_name": "Brecht",
    "last_name": "Voets",
    "password": "goodpassword15!",
    "registration_date": datetime.now(),
    "ID": 0
}
users = [user_brecht]


@app.get("/user")
def get_user(id: int = Query(default=None,gt=-1,
                             description="This parameter needs the private ID of an account to show more sensitive data.")):
    if id is not None and id < len(users):
        user = users[id]
        return user
    else:
        return {"error": "Not a valid ID!"}


@app.get("/users", response_model=list[Secure_User])
def get_users():
    return users


@app.post("/users/create")
def create_user(user: User):
    user.registration_date = datetime.now()
    user.ID = len(users)
    users.append(user)
    return user
