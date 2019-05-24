from flask.testing import FlaskClient

from app.factory import Factory


def test_factory_env_configuration():
    factory_app = Factory('testing')
    assert factory_app.environment == 'testing'
    factory_app.set_flask()
    factory_app.environment = 'development'
    assert factory_app.environment == 'development'

