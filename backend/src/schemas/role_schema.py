from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class RoleResponse(BaseModel):
    identifier: UUID
    enabled: bool
    registration_date: datetime
    last_update: datetime
    code: str
    name: str
