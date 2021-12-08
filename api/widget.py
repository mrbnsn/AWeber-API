'''Routes for the Widget API'''

from flask import abort, request, jsonify
from models import Widget, widget_schema, widgets_schema
from app import app, db


@app.route('/api/widget', methods=['POST'])
def create_widget():
    '''Create a new widget'''
    name = request.json.get('name')
    if name is None:
        raise KeyError('name')

    num_parts = request.json.get('num_parts')
    if num_parts is None:
        raise KeyError('num_parts')
    if not isinstance(num_parts, int):
        raise ValueError(
            'Bad Request - parameter num_parts must be of type int')

    widget = Widget(name, num_parts)
    db.session.add(widget)
    db.session.commit()

    return widget_schema.jsonify(widget)


@app.route('/api/widget/<widget_id>', methods=['GET'])
def get_widget(widget_id):
    '''Get a widget by ID'''
    widget = Widget.query.get(widget_id)

    if widget is None:
        abort(404, description=f"Widget with ID {widget_id} does not exist")

    return widget_schema.jsonify(widget)


@app.route('/api/widgets', methods=['GET'])
def list_widgets():
    '''List all widgets'''
    widgets = Widget.query.all()
    return jsonify(widgets_schema.dump(widgets))


@app.route('/api/widget/<widget_id>', methods=['PUT'])
def update_widget(widget_id):
    '''Update a widget'''
    widget = Widget.query.get(widget_id)

    if widget is None:
        abort(404, description=f"Widget with ID {widget_id} does not exist")

    name = request.json.get('name')
    if name is not None:
        widget.name = name

    num_parts = request.json.get('num_parts')
    if num_parts is not None:
        if not isinstance(num_parts, int):
            raise ValueError(
                'Bad Request - parameter num_parts must be of type int')
        widget.num_parts = num_parts

    db.session.commit()

    return widget_schema.jsonify(widget)


@app.route('/api/widget/<widget_id>', methods=['DELETE'])
def delete_widget(widget_id):
    '''Delete a widget by ID'''
    widget = Widget.query.get(widget_id)

    if widget is None:
        abort(404, description=f"Widget with ID {widget_id} does not exist")

    db.session.delete(widget)
    db.session.commit()

    return jsonify({"result": f"{widget.name} deleted"})
