"""Flask application instatiation, server entry point."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Define database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/later')
def hello2():
    return 'Once upon a World!'


if __name__ == "__main__":
    app.run(debug=True)
