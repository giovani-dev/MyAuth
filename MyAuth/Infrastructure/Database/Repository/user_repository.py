from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from peewee import DoesNotExist

from MyAuth.Application.Data.Dto.user import IsertUserDto, UpdateUserDto, UserDto
from MyAuth.Application.Database.Repository.user import IUserRepository
from MyAuth.Infrastructure.Database.Model.user import User


class UserRepository(IUserRepository):

    async def _make_dto(self, query: User) -> UserDto:
        return UserDto(
            id=query.external_id,
            name=query.name,
            email=query.email,
            cellphone=query.cellphone,
            user_name=query.user_name,
            creation_date=query.creation_date,
            updated_date=query.updated_date,
            is_adm=query.is_adm
        )

    async def create(
        self,
        data: IsertUserDto,
        is_adm: bool = False
    ) -> UserDto:
        if is_adm:
            query_by_email = User.get_or_none(
                User.email == data.email,
                User.is_adm == is_adm
            )
            query_by_cellphone = User.get_or_none(
                User.cellphone == data.cellphone,
                User.is_adm == is_adm
            )
            query_by_user_name = User.get_or_none(
                User.user_name == data.user_name,
                User.is_adm == is_adm
            )
            if query_by_user_name or query_by_cellphone or query_by_email:
                return None
        query = User.create(
            is_adm=is_adm,
            creation_date=datetime.now().replace(microsecond=0),
            external_id=uuid4(),
            **data.dict()
        )
        return await self._make_dto(query)

    async def update(
        self,
        id: uuid4,
        data: UpdateUserDto,
        is_adm: bool = False
    ) -> Optional[UserDto]:
        try:
            query = User.get(
                User.external_id == id,
                User.is_adm == is_adm
            )
        except DoesNotExist:
            return None

        if data.name:
            query.name = data.name
        if data.email:
            query.email = data.email
        if data.cellphone:
            query.cellphone = data.cellphone
        if data.user_name:
            query.user_name = data.user_name
        query.updated_date = datetime.now().replace(microsecond=0)

        query.save()
        return await self._make_dto(query)

    async def get_one_by_id(self, id: uuid4) -> Optional[UserDto]:
        query = User.get_or_none(User.external_id == id)
        if query:
            return await self._make_dto(query)
        return None

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

    async def delete(self, id: uuid4) -> bool:
        query = User.get_or_none(User.external_id == id)
        if query:
            query.delete_instance()
            return True
        return False
