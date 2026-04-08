from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import base

class Veterinario(base.Base):
  __tablename__ = "veterinario"

  id_vet = Column(Integer, primary_key = True)
  nome = Column(String, nullable = False)
