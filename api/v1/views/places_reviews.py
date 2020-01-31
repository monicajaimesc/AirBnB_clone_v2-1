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
    place = storage.get('Place', place_id)
    if place is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        reviews_list = [x.to_dict() for x in place.reviews]
        return make_response(jsonify(reviews_list), 200)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('user_id') is None:
            abort(400, 'Missing user_id')

        user = storage.get('User', data.get('user_id'))
        if user is None:
            abort(404, 'Not found')

        if data.get('text') is None:
            abort(400, 'Missing text')

        new_review = Review(**data)
        new_review.place_id = place.id
        new_review.user_id = user.id
        new_review.save()
        return make_response(jsonify(**new_review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def reviews(review_id):
    """
    Handle reviews by id
    """
    review = storage.get('Review', review_id)
    if review is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return make_response(jsonify(review.to_dict()), 200)

    elif request.method == 'PUT':
        changes = dict()

        try:
            changes = request.get_json()
            if changes is None:
                abort(400, 'Not a JSON')
        except BadRequest:
            abort(400, 'Not a JSON')

        ignores = ('id', 'user_id', 'place_id', 'created_at', 'updated_at')

        for key, val in changes.items():
            if key in ignores:
                pass
            else:
                setattr(review, key, val)

        review.save()
        return make_response(jsonify(**review.to_dict()), 200)

    elif request.method == 'DELETE':
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
