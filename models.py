from flask_sqlalchemy import SQLAlchemy

# STEP 2
#instantiate SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# models go below

# STEP 3

""""
class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        return f"< Pet, id = {self.id} name = {self.name} species = {self.species} hunger = {self.hunger}>"

    id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True)
    name = db.Column(db.String(50),
                    nullable = False,
                    unique = True)
    species = db.Column(db.String(30), nullable = True)
    hunger = db.Column(db.Integer, nullable = False, default = 20)

    # in terminal do ipython and run the command %run app.py then db.create_all() - you should see database table due to Echo config

    # add custom method to update database. method does not simply update database. You have to do db.session.add(instance), and db.session.commit()

    def feed(self, amt = 20):
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)  # if hunger goes to negative value- this converts that to zero

"""

""" SQLAlchemy Associations for multiple models in SQLAlchemy """

class Department(db.Model):
    """A department has many employees. """
    __tablename__ = "department"

    dept_code = db.Column(db.Text,
                            primary_key = True)
    dept_name = db.Column(db.Text,
                            nullable = False,
                            unique = True)
    phone = db.Column(db.Text)

class Employee(db.Model):
    """ Employee Model """
    __tablename__ = "employess"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False, unique = True)
    state = db.Column(db.Text, nullable = False, default = "CO")

# these tables are not connected, now connect them, may with foreign keys