from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class UserResponse(BaseModel):
    identifier: UUID
    enabled: bool
    registration_date: datetime
    last_update: datetime
    name: str
    username: str
    role_identifier: UUID
