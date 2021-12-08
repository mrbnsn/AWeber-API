from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# @TODO:
# Determine which fields to return for each request
# Use TYPE ANNOTATIONS
# PEP8
# Linter (flake8)
# Unit Tests
# OpenAPI spec file
# Pass Bandit security analysis

basedir: str = os.path.abspath(os.path.dirname(__file__))

# Init and configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import routes
from api import *

# Init SQLAlchemy
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Run server
if __name__ == '__main__':
    app.run(debug=True)