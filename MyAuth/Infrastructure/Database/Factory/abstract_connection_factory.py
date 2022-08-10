from typing import Optional
from MyAuth.Application.Database.Factory.abstract_connection_factory import AbstractConnectionFactory

from MyAuth.Application.Database.Factory.connection_factory import ConnectionFactory
from MyAuth.Application.Settings.enum import SqlDbType
from MyAuth.Application.Settings.settings import Settings
from MyAuth.Infrastructure.Database.Factory.connection_factory import MysqlConnection


class ConnectionAbcFactory(AbstractConnectionFactory):
    sql_connection_cache: Optional[ConnectionFactory] = None

    @classmethod
    def sql_connection(cls, db_type: SqlDbType) -> ConnectionFactory:
        if not cls.sql_connection_cache:
            match db_type:
                case SqlDbType.mysql:
                    database = MysqlConnection()
                    database.load(
                        db_name=Settings.database.db_name,
                        host=Settings.database.host,
                        user=Settings.database.user,
                        password=Settings.database.password,
                        port=Settings.database.port
                    )
                    cls.sql_connection_cache = database.connection
                    return cls.sql_connection_cache
                case SqlDbType.postgresql:
                    raise NotImplementedError()
                case default:
                    raise NameError("Cannot find sql db type for this use case.")
        else:
            return cls.sql_connection_cache
