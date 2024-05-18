#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the current SQLAlchemy Session after each request.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Renders an HTML page with a list of all State objects.
    """
    states = storage.all('State').values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
