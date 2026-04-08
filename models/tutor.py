from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import base

class Tutor(base.Base):
  __tablename__ = "tutores"

  id_tutor = Column(Integer, primary_key=True)
  nome = Column(String(100), nullable=False)
  telefone = Column(String(20), nullable=False)
  email = Column(String(100), unique=True, nullable=False)

  # animais = relationship("Animal", back_populates="cliente")
