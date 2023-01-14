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
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n is even|odd” inside the tag BODY
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
    return 'C ' + text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    '''Display "Python is cool"'''
    text = text.replace("_", " ")
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def display_n_number(n):
    '''Display "n is a number" if only n is a integer'''
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_n_template(n):
    '''Display a HTML page if only n is an integer'''
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_n_even_odd(n):
    '''Display a HTML page if only n is a integer even | odd'''
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
