
from typing import List, Optional
from uuid import uuid4
from MyAuth.Application.Data.Dto.claim import ClaimDto, InsertClaim, UpdateClaim

from MyAuth.Application.Database.Repository.claim import IClaimRepository
from MyAuth.Infrastructure.Database.Repository.Generic.generic_repository import GenericRepository


class ClaimRepository(IClaimRepository, GenericRepository):

    async def create(self, data: InsertClaim) -> ClaimDto:
        raise NotImplementedError()

    async def update(self, data: UpdateClaim) -> ClaimDto:
        raise NotImplementedError()

    async def get_one_by_id(self, id: uuid4) -> Optional[ClaimDto]:
        raise NotImplementedError()

    async def get_all(self, filter: object) -> List[Optional[ClaimDto]]:
        raise NotImplementedError()

    async def delete(self, id: uuid4) -> bool:
        raise NotImplementedError()
