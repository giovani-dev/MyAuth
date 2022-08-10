from MyAuth.Application.Database.Facade.repository_facade import RepositoryFacade
from MyAuth.Application.Database.Repository.claim import IClaimRepository
from MyAuth.Application.Database.Repository.role import IRoleRepository
from MyAuth.Application.Database.Repository.user import IUserRepository

from MyAuth.Infrastructure.Database.Model.claim import Claim
from MyAuth.Infrastructure.Database.Model.role import Role
from MyAuth.Infrastructure.Database.Model.user import User

from MyAuth.Infrastructure.Database.Repository.claim_repository import ClaimRepository
from MyAuth.Infrastructure.Database.Repository.role_repository import RoleRepository
from MyAuth.Infrastructure.Database.Repository.user_repository import UserRepository


class RepositoryFacade(RepositoryFacade):

    def user(self) -> IUserRepository:
        return UserRepository(User)

    def claim(self) -> IClaimRepository:
        return ClaimRepository(Claim)

    def role(self) -> IRoleRepository:
        return RoleRepository(Role)
