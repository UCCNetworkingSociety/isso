import json
from werkzeug.wrappers import Response


class JSONResponse(Response):

    def __init__(self, obj, *args, **kwargs):
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(
            json.dumps(obj).encode("utf-8"), *args, **kwargs)


class XMLResponse(Response):
    def __init__(self, obj, *args, **kwargs):
        kwargs["content_type"] = "text/xml"
        super(XMLResponse, self).__init__(
            obj, *args, **kwargs)
