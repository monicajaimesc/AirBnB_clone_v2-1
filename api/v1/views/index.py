#!/usr/bin/python3
"""
this file has the endpoint route
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


# convert as array
classes = ["Amenity", "City", "Place", "Review", "State", "User"]


@app_views.route('/status')
def json_status():
    """
    return a json file
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def endpoint_number_objects():
    """
    endpoint that retrieves the number
    of each objects by type:
    param cls: string representing the class name
    return: objects
    """
    object_classes = {"Amenity": "amenities",
                      "City": "cities",
                      "Place": "places",
                      "Review": "reviews",
                      "State": "states",
                      "User": "users"
                      }

    obj_return = {}
    for cls in classes:
        obj_return[object_classes[cls]] = storage.count(cls)
        print(obj_return)
    return jsonify(obj_return)



