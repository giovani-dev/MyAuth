from uuid import uuid4
from peewee import *

from MyAuth.Application.Settings.settings import Settings
from MyAuth.Infrastructure.Database.Factory.abstract_connection_factory import ConnectionAbcFactory


class BaseModel(Model):
    id = AutoField(column_name="Id", primary_key=True)
    external_id = CharField(column_name="ExternalId", max_length=36, unique=True, default=uuid4)
    creation_date = DateTimeField(column_name="CreationDate")
    updated_date = DateTimeField(column_name="UpdatedDate")

    class Meta:
        database = ConnectionAbcFactory.sql_connection(Settings.sql_db_type)