#!/usr/bin/python3
"""Status of API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route('/status')
def status():
    """Checks status of API"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def count_objs():
    """Counts number of objects in storage per Class"""
    d = {}
    d['amenities'] = storage.count(Amenity)
    d['cities'] = storage.count(City)
    d['places'] = storage.count(Place)
    d['reviews'] = storage.count(Review)
    d['states'] = storage.count(State)
    d['users'] = storage.count(User)
    return jsonify(d)
