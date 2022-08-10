from peewee import Model


class GenericRepository(object):
    _model: Model

    def __init__(self, model: Model) -> None:
        self._model = model
