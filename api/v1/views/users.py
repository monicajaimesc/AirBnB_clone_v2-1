#!/usr/bin/python3
"""
User objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.user import User
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def users():
    """
    Handle users in general
    """
    if request.method == 'GET':
        user_list = storage.all('User')
        user_return = []
        for value in user_list.values():
            user_return.append(value.to_dict())
        return jsonify(user_return)
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('email') is None:
            abort(400, 'Missing email')
        if data.get('password') is None:
            abort(400, 'Missing password')
        new_user = User(**data)
        new_user.save()
        return make_response(jsonify(**new_user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def user_by_id(user_id):
    """
    Handle user by id
    """
    user = storage.get('Amenity', user_id)
    if user is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return make_response(jsonify(user.to_dict()), 200)

    elif request.method == 'PUT':
        changes = dict()

        try:
            changes = request.get_json()
            if changes is None:
                abort(400, 'Not a JSON')
        except BadRequest:
            abort(400, 'Not a JSON')

        ignores = ('id', 'email',  'created_at', 'updated_at')

        for key, val in changes.items():
            if key in ignores:
                pass
            else:
                setattr(user, key, val)

        user.save()
        return make_response(jsonify(**user.to_dict()), 200)

    elif request.method == 'DELETE':
        storage.delete(user)
        storage.save()
        return make_response(jsonify({}), 200)
