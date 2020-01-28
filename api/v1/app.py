#!/usr/bin/python3
"""
this file will star an API
"""
from flask import Blueprint

from models import storage
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, threaded=True)