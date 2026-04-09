# from sqlalchemy import Column
# from config.database import SessionLocal, get_session
# from models.animal import Animal
#
# class AnimalService:
#
#   @staticmethod
#   def create_animal(data: dict[str, str]):
#     with SessionLocal() as s:
#
#       nome = data.get("nome")
#       especie = data.get("especie")
#       raca = data.get("raca")
#       sexo = data.get("sexo")
#       data_nascimento = data.get("data_nascimento")
#       id_animal = data.get("id_animal")
#
#       animal = Animal(nome = nome, especie = especie, raca = raca, sexo = sexo, data_nascimento = data_nascimento, id_animal = id_animal)
#
#       s.add(animal)
#       s.commit()
#       s.refresh(animal)
#       return animal
#
#   @staticmethod
#   def list_animais() -> list[Animal]:
#     with get_session() as s:
#       animais = s.query(Animal).all()
#       return animais
#
#   @staticmethod
#   def get_animal(animal_id: int) -> dict[str, str | int]:
#     with get_session() as s:
#       animal = s.query(Animal).get(animal_id) 
#       return  {"id": animal.id, "nome": animal.nome}
#
#   @staticmethod
#   def update_animal(animal_id: int, data: dict[str, str]) -> Animal | None:
#     with get_session() as s:
#
#       animal: Animal = s.query(Animal).get(animal_id)
#
#       new_nome: str = data.get("nome", "")
#       new_especie = data.get("especie", "")
#       new_raca = data.get("raca", "")
#       new_sexo = data.get("sexo", "")
#       new_data_nascimento = data.get("data_nascimento", "")
#       # Preciso criar "" para retornar um valor padrão
#
#       if animal is None:
#         return None
#
#       animal.nome = new_nome
#       especie = new_especie
#       raca = new_raca
#       sexo = new_sexo
#       data_nascimento = new_data_nascimento
#
#       s.commit()
#       return animal
#
#   @staticmethod
#   def delete_animal(animal_id: int):
#     with get_session() as s:
#       animal = s.get(Animal, animal_id)
#       s.delete(animal)
#       s.commit()
