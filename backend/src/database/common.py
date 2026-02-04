import abc


class BaseRepository(abc.ABC):

    @property
    @abc.abstractmethod
    def model_cls(self):
        return None

    def __init__(self, db):
        self.db = db

    @abc.abstractmethod
    def get_by_id(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
