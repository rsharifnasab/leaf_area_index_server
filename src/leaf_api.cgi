#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from leaf_api import app

CGIHandler().run(app)
