from sqlalchemy import Column
from config.database import SessionLocal
from models.tutor import Tutor

class TutorService:

  @staticmethod
  def create_tutor(data: dict[str, str]):
    with SessionLocal() as s:

      nome = data.get("nome")
      telefone = data.get("telefone")
      email = data.get("email")

      tutor = Tutor(nome = nome, telefone = telefone, email = email)
      s.add(tutor)
      s.commit()
      s.refresh(tutor)
      return tutor

  @staticmethod
  def list_tutores() -> list[dict[str, Column[int] | Column[str]]]:
    with get_session() as s:
      tutores = s.query(Tutor).all()
      resultado = [
          {"id": t.id, "nome": t.nome, "email": t.email}
          for t in tutores
          ]
      return resultado

  @staticmethod
  def get_tutor(tutor_id: int) -> dict[str, str | int]:
    with get_session() as s:
      tutor = s.query(Tutor).get(tutor_id) 
      return  {"id": tutor.id, "nome": tutor.nome}

  @staticmethod
  def update_tutor(tutor_id: int, data: dict[str, str]) -> Tutor | None:
    with get_session() as s:

      tutor: Tutor = s.query(Tutor).get(tutor_id)

      new_nome: str = data.get("nome", "") # Preciso criar "" para retornar um valor padrão
      new_telefone: str = data.get("telefone", "")
      new_email: str = data.get("email", "")

      if tutor is None:
        return None

      tutor.nome = new_nome
      tutor.telefone = new_telefone
      tutor.email = new_email

      s.commit()
      return tutor

  @staticmethod
  def delete_tutor(tutor_id: int):
    with get_session() as s:
      tutor = s.get(Tutor, tutor_id)
      s.delete(tutor)
      s.commit()
