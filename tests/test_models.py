from app.models import Example
from app.models.datastore import ExampleDatastore


def test_create_example(db):
    datastore = ExampleDatastore(db)
    datastore.create_example('test')

    ex = db.session.query(Example).filter_by(name='test').first()
    assert ex
