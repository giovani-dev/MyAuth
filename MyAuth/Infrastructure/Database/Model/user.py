from peewee import *

from MyAuth.Infrastructure.Database.Model.base_model import BaseModel
from MyAuth.Infrastructure.Database.Factory.abstract_connection_factory import ConnectionAbcFactory
from MyAuth.Application.Settings.settings import Settings


class User(BaseModel):
    name = CharField(column_name="Name", max_length=150)
    email = CharField(column_name="Email", max_length=125)
    password = CharField(column_name="Password", max_length=200)
    user_name = CharField(column_name="UserName", max_length=125)
    cellphone = CharField(column_name="Cellphone", max_length=45)
    is_adm = BooleanField(default=False, column_name='IsAdm')

    class Meta:
        database = ConnectionAbcFactory.sql_connection(Settings.sql_db_type)
        table_name = 'User'
