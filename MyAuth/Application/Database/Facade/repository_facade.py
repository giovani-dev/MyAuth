from abc import ABC, abstractmethod

from MyAuth.Application.Database.Repository.claim import IClaimRepository
from MyAuth.Application.Database.Repository.role import IRoleRepository
from MyAuth.Application.Database.Repository.user import IUserRepository



class RepositoryFacade(ABC):

    @abstractmethod
    def user(self) -> IUserRepository:
        raise NotImplementedError()

    @abstractmethod
    def claim(self) -> IClaimRepository:
        raise NotImplementedError()

    @abstractmethod
    def role(self) -> IRoleRepository:
        raise NotImplementedError()
