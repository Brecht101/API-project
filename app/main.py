import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/create") #, response_model=schemas.UserBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.registration_date = datetime.datetime.now()
    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=list[schemas.UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users", response_model=schemas.UserBase)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
