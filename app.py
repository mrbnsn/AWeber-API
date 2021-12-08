'''The main app file'''

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir: str = os.path.abspath(os.path.dirname(__file__))

# Init and configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init SQLAlchemy
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Import routes
from api import *

# Run server
if __name__ == '__main__':
    app.run()
