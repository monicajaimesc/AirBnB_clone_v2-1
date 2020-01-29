#!/usr/bin/python3
"""
Place objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'], strict_slashes=False)
def places_by_city(city_id):
    """
    Handle places by city
    """
    if request.method == 'GET':
        # TODO: Implement
        pass
    elif request.method == 'POST':
        # TODO: Implement
        pass


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def places(place_id):
    """
    Handle places in general
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
