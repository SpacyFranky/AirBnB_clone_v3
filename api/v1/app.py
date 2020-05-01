#!/usr/bin/python3
"""Status of API"""
import os
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.errorhandler(404)
def invalid_route(a):
    return jsonify({'error': 'Not found'})


@app.teardown_appcontext
def teardown(a):
    storage.close()

if __name__ == '__main__':
    app.run(host=os.getenv('HBNB_API_HOST'), port=os.getenv('HBNB_API_PORT'),
            threaded=True)