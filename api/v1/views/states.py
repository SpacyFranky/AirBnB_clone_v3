#!/usr/bin/python3
"""State objects that handles all default RestFul API actions"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.base_model import BaseModel
from models.state import State
from models import storage


@app_views.route('/states/', methods=['GET'])
def show_all():
    """Retrieves the list of all State objects"""
    states = storage.all(State)
    d = []
    for v in states.values():
        d.append(v.to_dict())
    return jsonify(d)


@app_views.route('/states/<state_id>', methods=['GET'],strict_slashes=False)
def show_by_id(state_id):
    """Retrieves a State object by id"""
    try:
        state = storage.get("State", state_id)
        j_state = state.to_dict()
        return jsonify(j_state)
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_by_id(state_id):
    """Deletes a State object"""
    states = storage.all(State)
    try:
        state = storage.get("State", state_id)
        storage.delete(state)
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create():
    """Creates a State"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    else:
        state_dict = request.get_json()
        if "name" in state_dict:
            state_name = state_dict["name"]
            state = State(name=state_name)
            for k, v in state_dict.items():
                setattr(state, k, v)
            state.save()
        else:
            abort(400)
            return jsonify({"error": "Missing name"})
        return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update(state_id):
    """Updates a State object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    req = request.get_json()
    for k, v in req.items():
        if k != "id" and k != "created_at" and k != "updated_at":
            setattr(state, k, v)
    state.save()
    return jsonify(state.to_dict()), 200
