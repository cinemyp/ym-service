from flask import Flask
from music import get_first_track

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/track')
def get_track():
    track = get_first_track()
    return track