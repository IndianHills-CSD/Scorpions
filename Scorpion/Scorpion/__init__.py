"""
The flask application package.
"""
from flask import Flask
application = app = Flask(__name__)

import Scorpion.views
