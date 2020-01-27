#!/usr/bin/python3
"""
this file will star
"""
from flask import Blueprint

from models import storage
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)



register the blueprint app_views to your Flask instance app
declare a method to handle @app.teardown_appcontext that calls storage.close()
inside if __name__ == "__main__":, run your Flask server (variable app) with:

