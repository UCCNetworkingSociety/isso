# -*- encoding: utf-8 -*-

from __future__ import division, unicode_literals

import pkg_resources
werkzeug = pkg_resources.get_distribution("werkzeug")

import hashlib
import json
import os

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest

from isso.compat import text_type
from isso.wsgi import Request

try:
    import ipaddress
except ImportError:
    import ipaddr as ipaddress
from ip import anonymize
from bloomfilter import Bloomfilter
from requests import JSONRequest
from render import render_template
from responses import JSONResponse, XMLResponse