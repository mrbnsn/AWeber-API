from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# @TODO:
# Validate params
# Determine which fields to return for each request
# Authenticate w/ basic auth
# Return HTTP status codes as appropriate
# Use TYPE ANNOTATIONS
# Handle out of range exceptions, etc
# Break into separate files/folders
# PEP8
# Linter (flake8)
# Unit Tests
# OpenAPI spec file
# Pass Bandit security analysis
# Import settings from config file

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init SQLAlchemy
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Widget Model
class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=False)
    num_parts = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name: str, num_parts: int):
        self.name = name
        self.num_parts = num_parts
        

# Widget Schema
class WidgetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'num_parts', 'created', 'updated')

# Init schema
widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many=True)

# Routes
@app.route('/widget', methods=['POST'])
def create_widget():
    '''Create a new widget'''
    name = request.json['name']
    num_parts = request.json['num_parts']

    widget = Widget(name, num_parts)

    db.session.add(widget)
    db.session.commit()

    return widget_schema.jsonify(widget)

@app.route('/widget/<id>', methods=['GET'])
def get_widget(id):
    '''Get a widget by ID'''
    widget = Widget.query.get(id) # ensure exists
    return widget_schema.jsonify(widget)

@app.route('/widgets', methods=['GET'])
def list_widgets():
    '''List all widgets'''
    widgets = Widget.query.all() # ensure exists, else return message indicating none
    return jsonify(widgets_schema.dump(widgets))

@app.route('/widget/<id>', methods=['PUT'])
def update_widget(id):
    '''Update a widget'''
    widget = Widget.query.get(id) # ensure exists

    name = request.json['name']
    num_parts = request.json['num_parts']

    widget.name = name
    widget.num_parts = num_parts

    # @TODO: only update fields that are passed (don't need to update all fields)

    db.session.commit()

    return widget_schema.jsonify(widget)

@app.route('/widget/<id>', methods=['DELETE'])
def delete_widget(id):
    '''Delete a widget by ID'''
    widget = Widget.query.get(id) # ensure exists
    db.session.delete(widget)
    db.session.commit()
    return jsonify({ "result": "Widget deleted"})

# Run server
if __name__ == '__main__':
    app.run(debug=True)