from datetime import datetime
import json
from uuid import uuid4

import bcrypt
from fastapi import APIRouter

from exceptions.fastapi_authentication_exceptions import InvalidCredentials
from middlewares.auth_middleware import generate_jwt
from schemas.auth_schema import LoginParameters, LoginResponse


auth_router = APIRouter()

@auth_router.post("/login", response_model=LoginResponse)
def login(
    parameters: LoginParameters
):
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)
        current_user = None
        for user in users:
            if user['username'] == parameters.username:
                current_user = user
                break
        if current_user is None or bcrypt.checkpw(parameters.password.encode('utf-8'), current_user['password'].encode('utf-8')) is False:
            raise InvalidCredentials()
        
    with open("roles.json", "r", encoding="utf-8") as f:
        roles = json.load(f)
        current_role = None
        for role in roles:
            if role['identifier'] == current_user['role_identifier']:
                current_role = role
                break
            
    return LoginResponse(
        role=current_role,
        user=current_user,
        access_token=generate_jwt(current_user['username'])
    )
