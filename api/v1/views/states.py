#!/usr/bin/python3
"""
State objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def view_states():
    """
   Resfult model (enpoints) that returns a list of states as arrays
   type(State): <class 'type'>
   properties:
            type: String, of class object
          created_at:
            type: string, The date the object created
          id:
            type: string, the id of the state
          name:
            type: string, name of the state
          updated_at:
            type: string, date when the object was updated
    returns:

   """
    if request.method == 'GET':
        states_ = storage.all('State')
        state_return = []
        for state in states_.values():
            state_return.append(state.to_dict())
        return jsonify(state_return)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('name') is None:
            abort(400, 'Missing name')
        new_state = State(**data)
        new_state.save()
        return make_response(jsonify(**new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def view_state_id(state_id=None):
    """
    shows an state for its id
    Properties:
    state_id[str]: id of the state selected

    Returns:

    """
    state = storage.get('State', state_id)
    if request.method == 'GET':
        if state:
            return jsonify(state.to_dict())
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

        target = storage.get('State', state_id)
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
        if state is None:
            abort(404, 'Not found')
        state = storage.get("State", state_id)
        if state_id is None:
            abort(404, 'Not found')
        storage.delete(state)
        return jsonify({}), 200

