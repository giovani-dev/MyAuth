from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import uuid4

from MyAuth.Application.Data.Dto.claim import ClaimDto, InsertClaim, UpdateClaim


class IClaimRepository(ABC):
    
    @abstractmethod
    async def create(self, data: InsertClaim) -> ClaimDto: ...

    @abstractmethod
    async def update(self, data: UpdateClaim) -> ClaimDto: ...

    @abstractmethod
    async def get_one_by_id(self, id: uuid4) -> Optional[ClaimDto]: ...

    @abstractmethod
    async def get_all(self, filter: object) -> List[Optional[ClaimDto]]: ...

    @abstractmethod
    async def delete(self, id: uuid4) -> bool: ...