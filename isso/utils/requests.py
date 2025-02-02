import pkg_resources
werkzeug = pkg_resources.get_distribution("werkzeug")
import json
from werkzeug.exceptions import BadRequest
from isso.wsgi import Request


class JSONRequest(Request):

    if werkzeug.version.startswith("0.8"):
        def get_data(self, **kw):
            return self.data.decode('utf-8')

    def get_json(self):
        try:
            return json.loads(self.get_data(as_text=True))
        except ValueError:
            raise BadRequest('Unable to read JSON request')
