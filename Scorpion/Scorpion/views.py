"""
Routes and views for the flask application.
"""

from datetime import datetime
import webbrowser
from flask import render_template
from Scorpion import app
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup

nav = Nav(app)

theNavBar = Navbar(
    'thenav',
    View('Home', 'home'),
    View('Esports', 'esports'),
    View('Sports', 'sports'),
    View('Movies', 'movies')
    )
nav.register_element('main_navbar', theNavBar)

@app.route('/')

@app.route('/home')
def home():
    """Renders the home page."""
    """
    queryString = "Monty Python"
    queryString = queryString.replace(" ", "%20", -1)
    IMDBQuery(queryString)
    """
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/esports')
def esports():
    """Renders the esports page."""
    return render_template(
        'Esports.html',
        title='Esports',
        year=datetime.now().year,
        message='Esports page.'
    )

@app.route('/sports')
def sports():
    """Renders the sports page."""
    str 
    return render_template(
        'Sports.html',
        title='Sports',
        year=datetime.now().year,
        message='Sports page.'
    )

@app.route('/movies')
def movies():
    """Renders the sports page."""
    str 
    return render_template(
        'Movies.html',
        title='Movies',
        year=datetime.now().year,
        message='Movies page.'
    )

def IMDBQuery(lookkupp):
    import http.client

    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "aacba34385msh2de2878b096e1a1p13e391jsn86c2163e469d"
        }

    conn.request("GET", "/title/auto-complete?q="+lookkupp, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
