from flask_sqlalchemy import SQLAlchemy

# STEP 2
#instantiate SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# models go below

# STEP 3

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True)
    name = db.Column(db.String(50),
                    nullable = False,
                    unique = True)
    species = db.Column(db.String(30), nullable = True)
    hunger = db.Column(db.Integer, nullable = False, default = 20)

    # in terminal do ipython and run the command %run app.py then db.create_all() - you should see database table due to Echo config
