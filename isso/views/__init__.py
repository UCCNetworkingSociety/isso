# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import pkg_resources
dist = pkg_resources.get_distribution("isso")

import json

from werkzeug.wrappers import Response
from werkzeug.routing import Rule
from werkzeug.exceptions import BadRequest

from isso import local
from isso.compat import text_type as str
from view import requires, Info