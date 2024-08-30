from flask import Flask
from flask_cors import CORS
from music import get_first_track

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/track')
def get_track():
    track = get_first_track()
    return track