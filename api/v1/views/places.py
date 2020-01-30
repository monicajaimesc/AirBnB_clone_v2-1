#!/usr/bin/python3
"""
Place objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.place import Place
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'], strict_slashes=False)
def places_by_city(city_id):
    """
    Handle places by city
    """
    if request.method == 'GET':
        places_ = storage.all('Place')
        place_return = []
        for place in places_.values():
            place_return.append(place.to_dict())
        return jsonify(place_return)
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('name') is None:
            abort(400, 'Missing name')
        new_places = Place(**data)
        new_places.save()
        return make_response(jsonify(**new_places.to_dict()), 201)
        


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def places(place_id):
    """
    Handle places in general
    """
    place = storage.get('Place', place_id)
    if request.method == 'GET':
        if place:
            return jsonify(place.to_dict())
        else:
            abort(404, 'Not found')
    elif request.method == 'PUT':
        changes = dict()

        try:
            changes = request.get_json()
            if changes is None:
                abort(400, 'Not a JSON')
        except BadRequest:
            abort(400, 'Not a JSON')
            
        target = storage.get('Place', place_id)
        if target is None:
            abort(404, 'Not found')

        ignores = ('id', 'created_at', 'updated_at')

        for key, val in changes.items():
            if key in ignores:
                pass
            else:
                setattr(target, key, val)

        target.save()
        return make_response(jsonify(**target.to_dict()), 200)
            
    elif request.method == 'DELETE':
        if place is None:
            abort(404, 'Not found')
        place = storage.get("Place", place_ids)
        if place_ids is None:
            abort(404, 'Not found')
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
