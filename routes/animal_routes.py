from flask import Blueprint, request
# from auth.decorator import auth_required, verify_permissions
from auth.decorator import auth_required, verify_role
from models.animal import Animal
from models.user import User_Types
from services.animal_service import AnimalService

animal_bp = Blueprint("animal_bp", __name__)

@animal_bp.route("/animal", methods=["POST"])
@auth_required
@verify_role([User_Types.ADM, User_Types.VET])
def criar():
    data = request.json
    animal = AnimalService.create_animal(data)
    return {"id":animal.id_animal, "nome":animal.nome}, 201

@animal_bp.route ("/animal", methods=["GET"])
@verify_role([User_Types.ADM, User_Types.VET])
def listar():
    animal = AnimalService.list_animais()
    return [
        {"id":a.id_animal, "nome":a.nome,"especie": a.especie, "raça": a.raca, "sexo": a.sexo, "Nascimento":a.data_nascimento}
        for a in animal
    ]

@animal_bp.route("/animal/<int:animal_id>", methods=["GET"])
@verify_role([User_Types.TUTOR, User_Types.ADM, User_Types.VET])
def obter(animal_id):
  animal = AnimalService.get_animal(animal_id)
  if not animal:
      return {"erro": "Animal não encontrado"}, 404
  return {"id":animal.id_animal, "nome":animal.nome, "especie":animal.especie, "raça":animal.raca, "sexo":animal.sexo, "Nascimento":animal.data_nascimento}


@animal_bp.route("/animal/<int:animal_id>", methods=["PUT"])
@verify_role([User_Types.ADM, User_Types.VET])
def atualizar (animal_id):
    data = request.json
    animal = AnimalService.update_animal(animal_id, data)
    if not animal:
        return {"erro": "Animal não encontrado"}, 404
    
    return {"id": animal.id_animal, "nome": animal.nome, "especie":animal.especie, "raça":animal.raca, "sexo":animal.sexo, "Nascimento":animal.data_nascimento}

@animal_bp.route("/animal/<int:animal_id>", methods=["DELETE"])
@auth_required
@verify_role([User_Types.ADM, User_Types.VET])
def deletar(animal_id):
    ok =AnimalService.delete_animal(animal_id)
    if not ok:
        return {"erro":"Animal não encontrado"}, 404
    return {"mensagem": "Animal removido com sucesso"}
