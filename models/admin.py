from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import base

class Admin(base.Base):
  __tablename__ = "admin"

  id = Column(Integer, primary_key = True)
