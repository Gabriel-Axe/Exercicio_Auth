from flask import Blueprint, request
from auth.decorator import verify_role
from models.tutor import Tutor
from models.user import User_Types
from services.tutor_service import TutorService


tutor_bp = Blueprint("tutor_bp", __name__)

@tutor_bp.route("/tutor", methods=["POST"])
@verify_role(User_Types.ADM)
def criar():
  data = request.json
  tutor: Tutor = TutorService.create_tutor(data)
  return {"id":tutor.id_tutor, "nome":tutor.nome}, 201

@tutor_bp.route("/tutor", methods=["GET"])
@verify_role([User_Types.ADM])
def listar():
  tutor = TutorService.list_tutores()
  return [
      {"id": t.id, "nome": t.nome, "telefone": t.telefone, "email":t.email}
      for t in tutor
      ]

@tutor_bp.route("/tutor/<int:tutor_id>", methods=["GET"])
@verify_role([User_Types.ADM, User_Types.VET])
def obter(tutor_id):
  tutor: Tutor = TutorService.get_tutor(tutor_id)
  if not tutor:
    return {"erro":"tutor não encontrado"}, 404

  return {"id":tutor.id, "nome": tutor.nome, "telefone":tutor.telefone, "email": tutor.email}


@tutor_bp.route("/tutor/<int:tutor_id>", methods=["PUT"])
@verify_role([User_Types.ADM])
def atualizar(tutor_id):
  data = request.json
  tutor: Tutor = TutorService.update_tutor(tutor_id, data)
  if not tutor:
    return {"erro": "tutor não existe"},404

  return {"id": tutor.id, "nome": tutor.nome, "telefone": tutor.telefone, "email": tutor.email}


@tutor_bp.route("/tutor/<int:tutor_id>", methods=["DELETE"])
@verify_role([User_Types.ADM])
def deletar(tutor_id):
  ok = TutorService.delete_tutor(tutor_id)
    if not ok:
      return {"erro": "tutor não existe"}, 404
    return {"mensagem": "tutor removido"}
