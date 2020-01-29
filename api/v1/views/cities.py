#!/usr/bin/python3
"""
City objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'], strict_slashes=False)
def cities_by_state(state_id):
    """
    Handle cities by state
    """
    if request.method == 'GET':
        # TODO: Implement
        pass
    elif request.method == 'POST':
        # TODO: Implement
        pass


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def cities(city_id):
    """
    Handle cities in general
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
