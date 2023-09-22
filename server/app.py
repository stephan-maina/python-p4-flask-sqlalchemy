#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI and disable tracking modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and associate it with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Run the Flask application on port 5555 in debug mode
    app.run(port=5555, debug=True)
