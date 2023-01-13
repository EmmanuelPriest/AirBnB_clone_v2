#!/usr/bin/python3
'''
Script that starts a Flask web application:
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    The option strict_slashes=False must be in the route definition
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display "HBNB"'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    '''Display "C " with the content of text'''
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    '''Display "Python is cool"'''
    text = text.replace("_", " ")
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
