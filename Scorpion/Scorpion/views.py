"""
Routes and views for the flask application.
"""

from datetime import datetime
import webbrowser
from flask import render_template
from Scorpion import app

import Scorpion.movieFunctions as mf
import Scorpion.eLeagueFunctions as el
import Scorpion.Sports as spt

'''This is a future thing that renders the navbar differently
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
'''

@app.route('/')

@app.route('/home')
def home():
    """Renders the home page."""
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
        message='Sports page.', 
        basketBallDesc = spt.getSport("Basketball"),
        footBallDesc = spt.getSport("American Football"),
        baseBallDesc = spt.getSport("Baseball")
    )

@app.route('/movies')
def movies():
    """Renders the sports page."""

    return render_template(
        'Movies.html',
        title='Movies',
        year=datetime.now().year,
        message='Movies page.'
    )


@app.route('/moviesResults')
def moviesResults():
    """Renders the sports page."""
    theSearchString = "Avengers"
    actualSearch = theSearchString.replace(" ", "%20", -1)

    return render_template(
        'MoviesResults.html',
        title='Movies',
        year=datetime.now().year,

        searchString = theSearchString,
        message='Movie search results.',
        movieResults = mf.movieSearch(actualSearch)
    )


@app.route('/LeagueOfLegends')
def LeagueOfLegends():
    """Renders the League page"""

    return render_template(
        'LeagueOfLegends.html',
        title="League of Legends",
        year=datetime.now().year,

        message='League of Legends page',
        # id pass
        leagueOfLegends = el.eLeagueFunctions()
        
    )





