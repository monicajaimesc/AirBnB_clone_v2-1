#!/usr/bin/python3
"""
Review objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'], strict_slashes=False)
def reviews_by_place(place_id):
    """
    Handle reviews by place
    """
    if request.method == 'GET':
        # TODO: Implement
        pass
    elif request.method == 'POST':
        # TODO: Implement
        pass


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def reviews(review_id):
    """
    Handle reviews by id
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
