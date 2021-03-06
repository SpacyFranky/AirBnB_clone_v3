#!/usr/bin/python3
"""State objects that handles all default RestFul API actions"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.base_model import BaseModel
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def show_all():
    """Retrieves the list of all State objects"""
    states = storage.all(State)
    d = []
    for v in states.values():
        d.append(v.to_dict())
    return jsonify(d)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def show_by_id(state_id):
    """Retrieves a State object by id"""
    states = storage.all(State)
    for v in states.values():
        if v.id == state_id:
            return jsonify(v.to_dict())
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_by_id(state_id):
    """Deletes a State object"""
    states = storage.all(State)
    for k, v in states.items():
        if v.id == state_id:
            storage.delete(v)
            storage.save()
            d = {}
            return jsonify(d), 200
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create():
    """Creates a State"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    d = request.get_json()
    if 'name' not in d.keys():
        abort(400, 'Missing name')
    n = State(**d)
    storage.save()
    return jsonify(n.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update(state_id):
    """Updates a State object"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    states = storage.all(State)
    for v in states.values():
        if v.id == state_id:
            d = request.get_json()
            for key, value in d.items():
                if key not in ('created_at', 'updated_at', 'id'):
                    setattr(v, key, value)
            storage.save()
            return jsonify(v.to_dict()), 200
    abort(404)
