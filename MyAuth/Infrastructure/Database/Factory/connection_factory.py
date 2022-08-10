from peewee import MySQLDatabase

from MyAuth.Application.Database.Factory.connection_factory import ConnectionFactory
from MyAuth.Application.Singleton.singleton import Singleton

# class MysqlConnection(ConnectionFactory, metaclass=Singleton):
class MysqlConnection(ConnectionFactory):
    connection: MySQLDatabase

    def load(self, db_name: str, user: str, password: str, host: str, port: int):
        self.connection = MySQLDatabase(
            db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.connection.connect()
