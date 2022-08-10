from datetime import datetime
from pydantic import BaseModel


class RoleDto(BaseModel):
    external_id: str
    creation_date: datetime
    updated_date: datetime
    name: str


class InsertRoleDto(BaseModel):
    external_id: str
    name: str


class UpdateRoleDto(BaseModel):
    name: str
