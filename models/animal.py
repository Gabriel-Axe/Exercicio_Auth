from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import base

class Animal(base.Base):
  __tablename__ = "animal"

  id_animal = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  especie = Column(String)
  raca = Column(String)
  sexo = Column(String)
  data_nascimento = Column(Date)
  id_tutor = Column(Integer, ForeignKey("tutor.id_tutor", ondelete="CASCADE"), nullable=False)
  tutor = relationship("Tutor", back_populates="animais")
