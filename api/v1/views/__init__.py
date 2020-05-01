#!/usr/bin/python3
"""Status of API"""
from flask import Blueprint

app_views = Blueprint(url_prefix='/api/v1', name='views_blueprint',
                      import_name=__name__)

from api.v1.views.index import *
