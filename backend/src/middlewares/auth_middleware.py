from datetime import datetime, timedelta, timezone
import json
import os

from dotenv import load_dotenv
import jwt
from fastapi import Security
from fastapi.security import APIKeyHeader

from exceptions.fastapi_authentication_exceptions import InvalidUserToken, UserBlocked, UserNotAuthenticated

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ISSUER = "POPUP_API"
AUDIENCE = "popup_frontend"

def generate_jwt(
    username: str,
    expires_delta: timedelta | None = None
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": username,
        "iat": now,
        "exp": now + (expires_delta or timedelta(days=1)),
        "iss": ISSUER,
        "aud": AUDIENCE
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt(token: str) -> str | None:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            issuer=ISSUER,
            audience=AUDIENCE
        )
        return payload
    except:
        return None

authorization_header = APIKeyHeader(name="Authorization")
async def get_current_user(
    authorization_header_value: str = Security(authorization_header)
):
    if not authorization_header_value or 'Bearer ' not in authorization_header_value:
        raise UserNotAuthenticated()

    access_token = authorization_header_value.split('Bearer ')[-1]
    response = verify_jwt(access_token)
    if response is None:
        raise InvalidUserToken()
    
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)
        for user in users:
            if user['username'] == response['sub']:
                current_user = user
                break

    if current_user is None:
        raise UserNotAuthenticated()
    
    if current_user.blocked is True:
        raise UserBlocked()

    return current_user
