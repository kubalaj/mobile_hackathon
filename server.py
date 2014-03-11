from flask import Flask, request, render_template

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint

from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/users.db'
db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    skill01 = db.Column(db.String)
    skill02 = db.Column(db.String)
    skill03 = db.Column(db.String)
    skill04 = db.Column(db.String)
    skill05 = db.Column(db.String)

    link01 = db.Column(db.String)
    link02 = db.Column(db.String)
    link03 = db.Column(db.String)

    imageLink01 = db.Column(db.String)
    imageLink02 = db.Column(db.String)

def CreateDummyData():
    n = User()
    n.name = 'Daniel'
    n.email = 'djmorrsee@gmail.com'
    n.skill01 = 'Python'
    n.skill02 = 'jQuery'
    n.skill03 = 'Flask'
    n.skill04 = 'SQL'
    n.skill05 = 'Cooking'

    n.link01 = 'http://www.google.com'
    n.link02 = 'http://www.facebook.com'
    n.link03 = 'http://www.reddit.com'

    n.imageLink01 = 'http://www.placehold.it/500x500'
    n.imageLink02 = 'http://www.placehold.it/500x500'

    db.session.add(n)
    db.session.commit()

@app.route('/')
@app.route("/home/")
def landing():
    return render_template('index.html')
    
@app.route('/portfolio')
def view_portfolio():
    users = User.query.all()
    return render_template('portfolio_view.html', info = users[0])

@app.route('/post', methods=['POST'])
def post_data():
    if request.method == 'POST':
        user = User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.skill01 = request.form['skill01']
        user.skill02 = request.form['skill02']
        user.skill03 = request.form['skill03']
        user.skill04 = request.form['skill04']
        user.skill05 = request.form['skill05']

        user.link01 = request.form['link01']
        user.link02 = request.form['link02']
        user.link03 = request.form['link03']

        user.imageLink01 = request.form['imageLink01']
        user.imageLink02 = request.form['imageLink02']

        db.session.add(user)
        db.session.commit()

@app.route('/templates')
def templates():    
    return render_template('templates.html')

if __name__ == "__main__":
    app.run(debug=True)


