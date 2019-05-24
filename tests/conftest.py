from gevent import monkey

monkey.patch_all(thread=False)

import psycogreen.gevent

psycogreen.gevent.patch_psycopg()


import pytest
from flask.testing import FlaskClient

from app import create_app
from .utils import JSONResponse


@pytest.fixture(scope='module')
def flask_app():
    app = create_app(environment='testing')
    from app.models.database import db

    with app.app_context():
        db.create_all()
        yield app
        db.session.close_all()
        db.drop_all()


@pytest.fixture(scope='module')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()


@pytest.fixture(scope='module')
def db(flask_app):
    from app.models.database import db as db_instance
    yield db_instance
