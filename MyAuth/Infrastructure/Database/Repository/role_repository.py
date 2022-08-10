from typing import List, Optional
from uuid import uuid4
from MyAuth.Application.Data.Dto.role import InsertRoleDto, RoleDto, UpdateRoleDto

from MyAuth.Application.Database.Repository.role import IRoleRepository
from MyAuth.Infrastructure.Database.Repository.Generic.generic_repository import GenericRepository


class RoleRepository(IRoleRepository, GenericRepository):

    async def create(self, data: InsertRoleDto) -> RoleDto:
        raise NotImplementedError()

    async def update(self, data: UpdateRoleDto) -> RoleDto:
        raise NotImplementedError()

    async def get_one_by_id(self, id: uuid4) -> Optional[RoleDto]:
        raise NotImplementedError()

    async def get_all(self, filter: object) -> List[Optional[RoleDto]]:
        raise NotImplementedError()

    async def delete(self, id: uuid4) -> bool:
        raise NotImplementedError()

