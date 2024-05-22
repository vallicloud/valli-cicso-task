import os 
from flask import Flask, render_template, request, session, redirect, url_for, flash 
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps                 # Python standard package 


# Defining the root directory for the rest of execution 
basedir = os.path.abspath(os.path.dirname(__file__))

# Creating Flask application object 
app = Flask(__name__)

# Setting arbitrary secret key for authentication & authorization 
app.secret_key = 'qwerty12345'

# Setting configuration flag for storing the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

# Creating SQLAlchemy database object
db = SQLAlchemy(app)


# Defining the structure of the table 
class MalwareURL(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self, url, status):
        self.url = url
        self.status = status

    def __repr__(self):
        return '{}'.format(self.status)

@app.route("/")
def welcome():
    return render_template('welcome.html') 


# Post log in landing page
@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/v1/urlinfo/all")
def view_all():
    malware_status = MalwareURL.query.all()
    return render_template("all.html", malware_status=malware_status)


