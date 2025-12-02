from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class DeviceFilterParameters(BaseModel):
    dependency_identifier: Optional[UUID] = None

class DeviceStatus(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

class DeviceResponse(BaseModel):
    identifier: UUID
    enabled: bool
    registration_date: datetime
    last_update: datetime
    dependency_identifier: UUID
    name: str
    status: DeviceStatus
    IP: str
    port: int
    last_connection: Optional[datetime] = None
    hostname: Optional[str] = None
    mac: Optional[str] = None
    operating_system: Optional[str] = None

class CreateDeviceParameters(BaseModel):
    dependency_identifier: UUID
    name: str
    IP: str
    port: int

class UpdateDeviceParameters(BaseModel):
    identifier: UUID
    dependency_identifier: Optional[UUID] = None
    name: Optional[str] = None
