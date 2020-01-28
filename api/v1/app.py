#!/usr/bin/python3
"""
this file will star an API
"""
from flask import Blueprint
from flask import jsonify

from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)

# Set CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(err):
    """
    Handles 404 error
    """
    context = {'error': str(err)}
    return jsonify(**context)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, threaded=True)
   host = getenv("HBNB_API_HOST", "0.0.0.0")
   port = getenv("HBNB_API_PORT", "5000")

