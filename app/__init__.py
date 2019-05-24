import click
from werkzeug.middleware.proxy_fix import ProxyFix

from .factory import Factory


def create_app(environment='development'):
    f = Factory(environment)
    f.set_flask()
    f.set_db()
    f.set_migration()
    f.set_api()

    # from models import Example

    app = f.flask

    from .views import sample_page

    app.register_blueprint(sample_page, url_prefix='/views')

    if app.config['TESTING']:  # pragma: no cover
        # Setup app for testing
        @app.before_first_request
        def initialize_app():
            pass

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE')

        return response

    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.cli.command()
    @click.argument('command')
    def setup(command):
        pass

    return app

