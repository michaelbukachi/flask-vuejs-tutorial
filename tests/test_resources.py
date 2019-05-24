from flask.testing import FlaskClient


def test_example_page(client: FlaskClient):
    res = client.get('/example')
    assert res.ok
    assert res.json == {'message': 'Success'}
