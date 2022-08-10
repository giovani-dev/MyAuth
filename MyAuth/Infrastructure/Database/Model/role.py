from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel


class Role(BaseModel):
    name = CharField(column_name="Name", max_length=45)
