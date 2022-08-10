from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ClaimDto(BaseModel):
    external_id: str
    creation_date: datetime
    updated_date: datetime
    name: str
    value: str


class InsertClaim(BaseModel):
    name: str
    value: str


class UpdateClaim(BaseModel):
    name: Optional[str]
    value: Optional[str]
