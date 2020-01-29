#!/usr/bin/python3
"""
this file will star an API
"""

from flask import jsonify, make_response
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

# Set CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(err):
    """
    Handles 404 error
    """
    context = {'error': 'Not found'}
    return make_response(jsonify(**context), 404)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, threaded=True)
