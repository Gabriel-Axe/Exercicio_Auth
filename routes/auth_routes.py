from flask import Blueprint, request
from models.user import User
from services.auth_service import AuthService

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register",methods=["POST"])
def register():
    data = request.json
    user: User = AuthService.register(data)
    return {"id": user.id, "email": user.email, "user role": user.type}, 201

@auth_bp.route("/login", methods = ["POST"])
def login():
   data = request.json
   user = AuthService.login(data)

   if not user:
        return {"erro":"credenciais inválidas"}, 401 
    
   return {"token": user.token}
