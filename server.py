from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(80), unique=False)
    skills = db.Column(db.String(80), unique=False)
    links = db.Column(db.String(80), unique=False)

    def __init__(self, name, email, skills, links):
        self.name = name
        self.email = email
        self.skills = skills
        self.links = links

    def __repr__(self):
        return '[name: %r, email:%r, skills:%r, links:%r]' % (
            self.name, self.email, self.skills, self.links)

@app.route('/')
@app.route("/home/")
def landing():
    return render_template('index.html')
    
@app.route('/portfolio')
def view_portfolio():    
    return render_template('portfolio_view.html')

@app.route('/templates')
def templates():    
    return render_template('templates.html')

if __name__ == "__main__":
    app.run(debug=True)

# name, email, social media, skills, links

h = [User('Steven McDude', 's.mcdude@gmail.com', 'C, C++, MATLAB, Heroku', 'github.com/eldeveloper, twitter.com/yosmark'),
User('Jennifer Vanek', 'j.vanek@gmail.com', 'Dancing, Goal Keeper, Stand-up comedian', 'www.facebook.com/something, www.json.com'),
User('John Appleseed', 'appleseed@apple.com', 'Writting, Painting, Archery', 'http://www.linkedin.com/12345, http://www.cs.colorado.edu')]

