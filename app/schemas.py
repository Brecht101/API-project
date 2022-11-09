from datetime import datetime

from pydantic import BaseModel


#class User(BaseModel):
 #   first_name: str
  #  last_name: str
   # password: str
    #registration_date: datetime | None = None  # User zou dit nu nog kunnen invullen, zou niet mogen
    #id: int | None = None  # zelfde hier


class User(BaseModel):
    first_name: str
    last_name: str
    registration_date: datetime | None = None
    id: int | None = None

class UserCreate(User):
    password: str
