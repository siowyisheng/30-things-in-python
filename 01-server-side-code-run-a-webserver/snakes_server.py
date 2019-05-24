# TO RUN
# $ export FLASK_APP=snakes_server.py
# $ flask run

from flask import Flask
app = Flask(__name__)


@app.route('/')
def snakey():
    return 'Slithering Ssssslytherin...'