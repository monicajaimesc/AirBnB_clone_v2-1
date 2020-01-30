#!/usr/bin/python3
"""
City objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.city import City
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'], strict_slashes=False)
def cities_by_state(state_id):
    """
    Handle cities by state
    """
    state = storage.get('State', state_id)
    if state is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        city_list = [x.to_dict() for x in state.cities]
        return make_response(jsonify(city_list), 200)

    elif request.method == 'POST':
        try:
            data = request.get_json()
            if data is None:
                abort(400, 'Not a JSON')
            if data.get('name') is None:
                abort(400, 'Missing name')
            new_city = City(**data)
            new_city.state_id = state_id
            new_city.save()
            return make_response(jsonify(**new_city.to_dict()), 201)
        except BadRequest:
            abort(400, 'Not a JSON')


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def cities(city_id):
    """
    Handle cities in general
    """
    city = storage.get('City', city_id)
    if city is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return make_response(jsonify(city.to_dict()), 200)

    elif request.method == 'PUT':
        changes = dict()

        try:
            changes = request.get_json()
            if changes is None:
                abort(400, 'Not a JSON')
        except BadRequest:
            abort(400, 'Not a JSON')

        ignores = ('id', 'created_at', 'updated_at')

        for key, val in changes.items():
            if key in ignores:
                pass
            else:
                setattr(city, key, val)

        city.save()
        return make_response(jsonify(**city.to_dict()), 200)

    elif request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return make_response(jsonify({}), 200)
