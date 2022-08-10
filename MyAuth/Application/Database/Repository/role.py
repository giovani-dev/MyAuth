from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import uuid4

from MyAuth.Application.Data.Dto.role import InsertRoleDto, RoleDto, UpdateRoleDto



class IRoleRepository(ABC):

    @abstractmethod
    async def create(self, data: InsertRoleDto) -> RoleDto: ...

    @abstractmethod
    async def update(self, data: UpdateRoleDto) -> RoleDto: ...

    @abstractmethod
    async def get_one_by_id(self, id: uuid4) -> Optional[RoleDto]: ...

    @abstractmethod
    async def get_all(self, filter: object) -> List[Optional[RoleDto]]: ...

    @abstractmethod
    async def delete(self, id: uuid4) -> bool: ...