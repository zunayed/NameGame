from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zunayed:password@localhost/namegame'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    profile_picture = db.Column(db.String(140))
    correct_picks = db.Column(db.Integer)
    incorrect_picks = db.Column(db.Integer)

    def __init__(self, username, link):
        self.username = username
        self.profile_picture = link
        self.correct_picks = 0
    	self.incorrect_picks = 0
