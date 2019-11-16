#main.py
from tracks.api.flask_headless_rest_api.track_server import blueprint as track_server_bl
from flask import Flask

def create_app(debug=True):
    app = Flask(__name__)
    app.register_blueprint(track_server_bl)