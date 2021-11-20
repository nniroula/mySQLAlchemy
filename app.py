from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet  # db is instance db = SQLAlchemy()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example' # movies is a database name

# STEP 3 change database name in URI to associate with new database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db' # 


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress the warning message you get when you run app.py file

app.config['SQLALCHEMY_ECHO'] = True  # this shows all sql commands being executed in ipython terminal when you run db.session.execute('select * from movies') like command

# STEP 2
# db = SQLAlchemy()
# db.app = app # To associate our app with SQLAlchemy
# db.init_app(app)

app.config['SECRET_KEY'] = "nkbhaiebro"
debug = DebugToolbarExtension(app)

connect_db(app)   # STEP 2

@app.route('/')
def home():
    """ shows home page"""
    return render_template("home.html")
    # return "Hello, sqlAlchemy experts"