#!/usr/bin/python3
"""
Amenity objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def amenities():
    """
    Handle amenities in general
    """
    if request.method == 'GET':
        amenity_list = storage.all('Amenity')
        amenity_return = []
        for value in amenity_list.values():
            amenity_return.append(value.to_dict())
        return jsonify(amenity_return)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('name') is None:
            abort(400, 'Missing name')
        new_amenity = Amenity(**data)
        new_amenity.save()
        return make_response(jsonify(**new_amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def amenities_by_id(amenity_id):
    """
    Handle amenity by id
    """
    amenity = storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return make_response(jsonify(amenity.to_dict()), 200)

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
                setattr(amenity, key, val)

        amenity.save()
        return make_response(jsonify(**amenity.to_dict()), 200)

    elif request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()
        return make_response(jsonify({}), 200)
