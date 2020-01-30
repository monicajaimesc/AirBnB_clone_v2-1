#!/usr/bin/python3
"""
Review objects that will handles all default RestFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.review import Review
from flask import jsonify, abort, request, make_response
from werkzeug.exceptions import BadRequest


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'],
                 strict_slashes=False)
def reviews_by_place(place_id):
    """
    Handle reviews by place
    """
    if request.method == 'GET':
        review_ = storage.all('Review')
        review_return = []
        for review in review_.values():
            review_return.append(review.to_dict())
        return jsonify(review_return)
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('name') is None:
            abort(400, 'Missing name')
        new_review = Review(**data)
        new_review.save()
        return make_response(jsonify(**new_review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def reviews(review_id):
    """
    Handle reviews by id
    """
    review = storage.get('Review', review_id)
    if request.method == 'GET':
        if review:
            return jsonify(review.to_dict())
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

        target = storage.get('Review', review_id)

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
        if review is None:
            abort(404, 'Not found')
        review = storage.get("Review", review_id)
        if review_id is None:
            abort(404, 'Not found')
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
