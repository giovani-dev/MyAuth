from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from MyAuth.Application.Data.Dto.user import IsertUserDto, UpdateUserDto, UserDto

from MyAuth.Application.Database.Repository.user import IUserRepository
from MyAuth.Infrastructure.Database.Model.user import User
from MyAuth.Infrastructure.Database.Repository.Generic.generic_repository import GenericRepository


class UserRepository(IUserRepository, GenericRepository):

    async def _make_dto(self, query: User) -> UserDto:
        return UserDto(
            id=query.external_id,
            name=query.name,
            email=query.email,
            cellphone=query.cellphone,
            user_name=query.user_name,
            creation_date=query.creation_date,
            updated_date=query.updated_date
        )

    async def create(self, data: IsertUserDto, is_adm: bool) -> UserDto:
        query = User.create(
            is_adm=is_adm,
            creation_date=datetime.now().replace(microsecond=0),
            **data.dict()
        )
        return await self._make_dto(query)

    async def update(self, id: uuid4, data: UpdateUserDto) -> UserDto:
        raise NotImplementedError()

    async def get_one_by_id(self, id: uuid4) -> Optional[UserDto]:
        raise NotImplementedError()

    async def get_one_by_email(self, email: str) -> Optional[UserDto]:
        query = User.get_or_none(User.email == email)
        if query:
            return await self._make_dto(query)
        return None

    async def get_one_by_user_name(self, user_name: str) -> Optional[UserDto]:
        query = User.get_or_none(User.user_name == user_name)
        if query:
            return await self._make_dto(query)
        return None

    async def get_all(self, filter: object) -> List[Optional[UserDto]]:
        raise NotImplementedError()

    async def delete(self, id: uuid4) -> bool:
        raise NotImplementedError()
