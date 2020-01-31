#!/usr/bin/python3
"""
Place objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.place import Place
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'],
                 strict_slashes=False)
def places_by_city(city_id):
    """
    Handle places by city
    """
    city = storage.get('City', city_id)
    if city is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        places_list = [x.to_dict() for x in city.places]
        return make_response(jsonify(places_list), 200)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('user_id') is None:
            abort(400, 'Missing user_id')

        user = storage.get('User', data.get('user_id'))
        if user is None:
            abort(404, 'Not found')

        if data.get('name') is None:
            abort(400, 'Missing name')

        new_place = Place(**data)
        new_place.city_id = city.id
        new_place.user_id = user.id
        new_place.save()
        return make_response(jsonify(**new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def places(place_id):
    """
    Handle places in general
    """
    place = storage.get('Place', place_id)
    if place is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return make_response(jsonify(place.to_dict()), 200)

    elif request.method == 'PUT':
        changes = dict()

        try:
            changes = request.get_json()
            if changes is None:
                abort(400, 'Not a JSON')
        except BadRequest:
            abort(400, 'Not a JSON')

        ignores = ('id', 'user_id', 'city_id', 'created_at', 'updated_at')

        for key, val in changes.items():
            if key in ignores:
                pass
            else:
                setattr(place, key, val)

        place.save()
        return make_response(jsonify(**place.to_dict()), 200)

    elif request.method == 'DELETE':
        storage.delete(place)
        storage.save()
        return make_response(jsonify({}), 200)
