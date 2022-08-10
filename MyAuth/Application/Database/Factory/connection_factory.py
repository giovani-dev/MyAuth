
from abc import ABC, abstractmethod


class ConnectionFactory(ABC):
    connection: object

    @abstractmethod
    def load(self, db_name: str, user: str, password: str, host: str, port: int): ...
