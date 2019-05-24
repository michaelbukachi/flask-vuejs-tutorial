import json

from flask import Response
from werkzeug.utils import cached_property


class JSONResponse(Response):

    @cached_property
    def json(self):
        return json.loads(self.get_data(as_text=True))

    @cached_property
    def conflict(self):
        return self.status_code == 409

    @cached_property
    def not_found(self):
        return self.status_code == 404

    @cached_property
    def bad_args(self):
        return self.status_code == 400

    @cached_property
    def unauthorized(self):
        return self.status_code in {401, 403}

    @cached_property
    def ok(self):
        return self.status_code in {200, 201}

    @cached_property
    def oops(self):
        return self.status_code == 422


def do_nothing(*args, **kwargs):
    pass
