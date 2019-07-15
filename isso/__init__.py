#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2012-2014 Martin Zimmermann.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Isso – a lightweight Disqus alternative

from __future__ import print_function, unicode_literals

import pkg_resources
dist = pkg_resources.get_distribution("isso")

# check if exectuable is `isso` and gevent is available
import sys

if sys.argv[0].startswith("isso"):
    try:
        import gevent.monkey
        gevent.monkey.patch_all()
    except ImportError:
        pass

import os
import errno
import logging
import tempfile

from os.path import dirname, join
from argparse import ArgumentParser
from functools import partial, reduce

import pkg_resources
werkzeug = pkg_resources.get_distribution("werkzeug")

from itsdangerous import URLSafeTimedSerializer

from werkzeug.routing import Map
from werkzeug.exceptions import HTTPException, InternalServerError

from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.local import Local, LocalManager
from werkzeug.serving import run_simple
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.contrib.profiler import ProfilerMiddleware

local = Local()
local_manager = LocalManager([local])

from isso import config, db, migrate, wsgi, ext, views
from isso.core import ThreadedMixin, ProcessMixin, uWSGIMixin
from isso.wsgi import origin, urlsplit
from isso.utils import http, JSONRequest, html, hash
from isso.views import comments

from isso.ext.notifications import Stdout, SMTP

from main import Isso, make_app, main
