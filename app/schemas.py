from datetime import datetime

from pydantic import BaseModel



class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str
    registration_date: datetime | None = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True