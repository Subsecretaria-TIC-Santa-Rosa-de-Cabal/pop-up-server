from pydantic import BaseModel

from schemas.role_schema import RoleResponse
from schemas.user_schema import UserResponse


class LoginResponse(BaseModel):
    role: RoleResponse
    user: UserResponse
    access_token: str

class LoginParameters(BaseModel):
    username: str
    password: str
