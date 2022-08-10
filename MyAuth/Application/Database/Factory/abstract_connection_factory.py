from abc import ABC, abstractclassmethod, abstractmethod

from MyAuth.Application.Database.Factory.connection_factory import ConnectionFactory
from MyAuth.Application.Settings.enum import SqlDbType


class AbstractConnectionFactory(ABC):

    @abstractclassmethod
    def sql_connection(cls, db_type: SqlDbType) -> ConnectionFactory: ...
