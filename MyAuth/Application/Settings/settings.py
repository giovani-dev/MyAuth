
from email.policy import default
import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel

from MyAuth.Application.Settings.enum import SqlDbType


class Database(BaseModel):
    db_name: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None


class Settings(object):
    database: Database = Database()
    sql_db_type: Optional[SqlDbType] = None

    @staticmethod
    def load():
        if(os.getenv('APP_ENV') == 'local' or not os.getenv('APP_ENV')):
            load_dotenv()
        Settings.database.db_name = os.getenv('DB_NAME')
        Settings.database.user = os.getenv('DB_USER')
        Settings.database.password = os.getenv('DB_PASSWORD')
        Settings.database.host = os.getenv('DB_HOST')
        Settings.database.port = int(os.getenv('DB_PORT'))

        database_type = os.getenv('DB_SQL_TYPE')

        match database_type:
            case "mysql":
                Settings.sql_db_type = SqlDbType.mysql
            case "postgresql":
                Settings.sql_db_type = SqlDbType.postgresql
            case default:
                raise NotImplementedError(f'This {database_type} database is not implemented')