from flask import jsonify, request, g
from functools import wraps
from models.user import User_Types
from services.auth_service import AuthService
from services.tutor_service import TutorService

def auth_required(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Token "):
      return {"erro": f"Token ausente ou invalido: {auth_header}"}, 401

    token = auth_header.split(" ")[1]
    user = AuthService.get_user_by_token(token)

    if not user:
      return {"erro": "Token inválido"}, 401

    g.current_user = user
    return f(*args, **kwargs)

  return wrapper

def verify_role(*allowed_roles: list[User_Types]):
  def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

      auth_header = request.headers.get("Authorization")
      if not auth_header:
        return jsonify({"erro": "Token ausente"}), 401

      token = auth_header.split(" ")[1]
      user = AuthService.get_user_by_token(token)

      user_type = None
      match user.type:
        case User_Types.TUTOR.value:
          user_type = User_Types.TUTOR
        case User_Types.VET.value:
            user_type = User_Types.VET
        case User_Types.ADM.value:
          user_type = User_Types.ADM
        case _:
          pass

      if not user:
        return jsonify({"erro": "Token inválido ou não encontrado"})

      if user_type == None or user_type not in allowed_roles:
        return {"erro": f"Usuário não autorizado\nAutorizados: {[a.name for a in allowed_roles]}\nEnviado: {user_type.name}"}, 403

      return f(*args, **kwargs)
    return wrapper
  return decorator
