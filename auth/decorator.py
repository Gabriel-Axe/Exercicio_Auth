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
      return {"erro": "Token ausente ou invalido"}, 401

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

      if not user:
        return jsonify({"erro": "Token inválido ou não encontrado"})

      if user.type not in allowed_roles:
        return {"erro": "Usuário não autorizado"}, 403

      return f(*args, user=user, **kwargs)
    return wrapper
  return decorator
