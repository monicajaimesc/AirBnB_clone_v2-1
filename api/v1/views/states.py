#!/usr/bin/python3
"""
States view
"""

from models import storage
from api.v1.views import app_views
from flask import request, jsonify, abort


@app_views.route('/states', method=['GET', 'POST'])
def states():
    # TODO: Add states Requests and remove pass (request.get_json() gets the data)
    pass


@app_views.route('/states/<id>', method=['GET', 'DELETE', 'PUT'])
def states_by_id(id=None):
    # TODO: Add requests by id (use flask request to check method, abort to return error), remove pass
    pass
