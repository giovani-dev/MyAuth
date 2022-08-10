from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel
from MyAuth.Infrastructure.Database.Model.claim import Claim
from MyAuth.Infrastructure.Database.Model.role import Role


class RoleClaim(BaseModel):
    role = ForeignKeyField(Role, column_name='Role', lazy_load=False)
    claim = ForeignKeyField(Claim, column_name='Role', lazy_load=False)
