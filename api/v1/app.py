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
app.url_map.strict_slashes = False

@app.errorhandler(404)
def invalid_route(a):
    """returns a JSON-formatted 404 status code response"""
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown(a):
    """calls storage close function"""
    storage.close()

if __name__ == '__main__':
    app.run(host=os.getenv('HBNB_API_HOST'), port=os.getenv('HBNB_API_PORT'),
            threaded=True)
