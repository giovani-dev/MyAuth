from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class UserDto(BaseModel):
    id: UUID
    name: str
    email: str
    cellphone: str
    user_name: str
    creation_date: datetime
    updated_date: Optional[datetime]


class IsertUserDto(BaseModel):
    name: str
    email: str
    cellphone: str
    user_name: str
    password: str
    password_verification: str


class UpdateUserDto(BaseModel):
    name: Optional[str]
    email: Optional[str]
    cellphone: Optional[str]
    user_name: Optional[str]
    updated_date: Optional[datetime]
