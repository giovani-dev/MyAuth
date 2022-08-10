from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel


class Claim(BaseModel):
    name = CharField(column_name="Name", max_length=45)
    value = CharField(column_name="Value", max_length=45)
