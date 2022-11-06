# API voor users met passwoorden opgeslagen in db + hashing?

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from datetime import datetime
import mysql.connector

app = FastAPI()



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="passW1$!",
  database='users'
)

mycursor = mydb.cursor()
mycursor.execute("create table data(firstname varchar(100), lastname varchar(100), password varchar(100), registration_date datetime, id int)")

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
users = []

sql = "INSERT INTO data (firstname, lastname, password, registration_date, id) VALUES (%s, %s, %s, %s, %s)"
val = ("Brecht", "Voets", "goodpassword15!", datetime.now(), 0)
#mycursor.execute(sql, val)
mydb.commit()

@app.get("/user")
def get_user(id: int = Query(default=None,gt=-1,
                             description="This parameter needs the private ID of an account to show more sensitive data.")):
    if id is not None: #and id < len(users):
        #user = users[id]
        #return user
        sql = "SELECT * from data where id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return result

    else:
        return {"error": "Not a valid ID!"}


@app.get("/users")
def get_users():
    mycursor.execute("SELECT firstname, lastname, registration_date, id FROM data")

    myresult = mycursor.fetchall()

    return myresult


@app.post("/users/create")
def create_user(user: User):
    user.registration_date = datetime.now()
    user.ID = len(users)
    users.append(user)
    sql = "INSERT INTO data (firstname, lastname, password, registration_date, id) VALUES (%s, %s, %s, %s, %s)"
    val = (user.first_name, user.last_name, user.password, datetime.now(), len(users))
    mycursor.execute(sql, val)
    mydb.commit()
    return user
