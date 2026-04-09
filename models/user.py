from enum import Enum
from sqlalchemy import Column, Integer, String
from . import base

class User_Types(Enum):
  ADM = 1
  VET = 2
  TUTOR = 3

class User(base.Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  email = Column(String, unique=True, nullable=False)
  password_hash = Column(String, nullable=False)
  token = Column(String, nullable=False)
  type = Column(Integer, nullable=False)
