from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class User(Base):
    __tablename__ = "data"

    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    registration_date = Column(datetime) #datetime?
    id = Column(Integer, primary_key=True, index=True)
