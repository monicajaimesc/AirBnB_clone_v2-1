#!/usr/bin/python3
"""
User objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def users():
    """
    Handle users in general
    """
    if request.method == 'GET':
        # TODO: Implement
        pass
    elif request.method == 'POST':
        # TODO: Implement
        pass


@app_views.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def user_by_id(user_id):
    """
    Handle user by id
    """
    if request.method == 'GET':
        # TODO: Implement
        pass
    elif request.method == 'PUT':
        # TODO: Implement
        pass
    elif request.method == 'DELETE':
        # TODO: Implement
        pass
