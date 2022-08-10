from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel


class User(BaseModel):
    name = CharField(column_name="Name", max_length=150)
    email = CharField(column_name="Email", max_length=125)
    password = CharField(column_name="Password", max_length=200)
    user_name = CharField(column_name="UserName", max_length=125)
    cellphone = CharField(column_name="Cellphone", max_length=45)
