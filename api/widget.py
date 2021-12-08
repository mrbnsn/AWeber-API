from flask import request, jsonify
from models import Widget, widget_schema, widgets_schema
from app import app, db

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