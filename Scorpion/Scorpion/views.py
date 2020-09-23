"""
Routes and views for the flask application.
"""

from datetime import datetime
import webbrowser
from flask import render_template
from Scorpion import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    queryString = "Monty Python"
    queryString = queryString.replace(" ", "%20", -1)
    IMDBQuery(queryString)
    return render_template(
        'Esports.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    str 
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
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
