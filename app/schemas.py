from datetime import datetime

from pydantic import BaseModel


#class User(BaseModel):
 #   first_name: str
  #  last_name: str
   # password: str
    #registration_date: datetime | None = None  # User zou dit nu nog kunnen invullen, zou niet mogen
    #id: int | None = None  # zelfde hier


class UserBase(BaseModel):
    first_name: str
    last_name: str
    registration_date: datetime | None = None
    id: int | None = None


class UserCreate(UserBase):
    password: str

class User(UserBase):
    first_name: str
    last_name: str
    registration_date: datetime | None = None

    class Config:
        orm_mode = True