from abc import ABC

from .base import Example


class Datastore(ABC):

    def __init__(self, _db=None):
        self.session = None
        if _db:
            self.session = _db.session


class ExampleDatastore(Datastore):

    def __init__(self, _db):
        super().__init__(_db)

    def create_example(self, name):
        ex = Example(name=name)
        self.session.add(ex)
        self.session.commit()
