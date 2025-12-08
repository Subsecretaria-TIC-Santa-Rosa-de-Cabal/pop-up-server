from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


class LunchPopupParameters(BaseModel):
    name: str
    description: str
    date: datetime
    image_base64: Optional[str] = None
    dependency_identifier: Optional[UUID] = None

class PopupLunchResponse(BaseModel):
    identifier: UUID
    enabled: bool
    registration_date: datetime
    last_update: datetime
    name: str
    description: str
    date: datetime
    device_identifiers: List[UUID]
    image_path: Optional[str] = None
    dependency_identifier: Optional[UUID] = None
