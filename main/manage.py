"""Flask application instatiation, server entry point."""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
app = Flask(__name__, template_folder='../templates')

# Define database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

from trial.models import User


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    exists = User.query.filter_by(username=username).first()
    if username and password:
        if exists:
            return redirect('/')
        new_user = User(username=username, email=email)
        new_user.hash_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/later')
        except SQLAlchemyError:
            db.session.rollback()
        return redirect(url_for('main'))


@app.route('/later')
def hello2():
    return 'Once upon a World!'
