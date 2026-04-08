from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import base

class User(base.Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  email = Column(String, unique=True, nullable=False)
  password_hash = Column(String, nullable=False)
  token = Column(String)
