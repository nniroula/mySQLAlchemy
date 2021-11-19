from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'Postgresql:///movies' # movies is a database name

db = SQLAlchemy()
db.app = app # To associate our app with SQLAlchemy
db.init_app(app)
