from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel
from MyAuth.Infrastructure.Database.Model.user import User


class SubalternUser(BaseModel):
    adm_user = ForeignKeyField(User, column_name='AdmUser', lazy_load=False, on_delete='CASCADE')
    user = ForeignKeyField(User, column_name='User', lazy_load=False, on_delete='CASCADE')
