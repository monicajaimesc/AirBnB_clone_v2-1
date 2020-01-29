#!/usr/bin/python3
"""
State objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify,abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
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
    states_ = storage.all('State')
    state_return = []
    for state in states_.values():
        state_return.append(state.to_dict())
    return jsonify(state_return)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def view_state_id(state_id=None):
    """
    shows an state for its id
    Properties:
    state_id[str]: id of the state selected

    Returns:

    """
    state = storage.get('State', state_id)
    if state:
        return jsonify(state.to__dict())
    else:
        abort(404)




