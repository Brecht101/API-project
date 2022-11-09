from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from database import Base


class User(Base):
    __tablename__ = "data"

    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(50))
    registration_date = Column(DateTime) #datetime?
    id = Column(Integer, primary_key=True, index=True)
