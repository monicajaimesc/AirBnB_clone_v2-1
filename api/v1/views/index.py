#!/usr/bin/python3
"""
this file has the endpoint route
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def json_status():
    """
    return a json file
    """
    return jsonify({"status": "OK"})