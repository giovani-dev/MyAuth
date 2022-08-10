from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import uuid4

from MyAuth.Application.Data.Dto.user import IsertUserDto, UpdateUserDto, UserDto


class IUserRepository(ABC):

    @abstractmethod
    async def create(self, data: IsertUserDto, is_adm: bool) -> UserDto: ...

    @abstractmethod
    async def update(self, id: uuid4, data: UpdateUserDto) -> UserDto: ...

    @abstractmethod
    async def get_one_by_id(self, id: uuid4) -> Optional[UserDto]: ...

    @abstractmethod
    async def get_one_by_email(self, email: str) -> Optional[UserDto]: ...

    @abstractmethod
    async def get_one_by_user_name(self, user_name: str) -> Optional[UserDto]: ...

    @abstractmethod
    async def get_all(self, filter: object) -> List[Optional[UserDto]]: ...

    @abstractmethod
    async def delete(self, id: uuid4) -> bool: ...
