from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class DependencyResponse(BaseModel):
    identifier: UUID
    enabled: bool
    registration_date: datetime
    last_update: datetime
    name: str
    devices_count: int

class CreateDependencyParameters(BaseModel):
    name: str

class CreateDependencyParameters(BaseModel):
    name: str

class UpdateDependencyParameters(BaseModel):
    identifier: UUID
    name: str
