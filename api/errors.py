from flask import jsonify
from app import app

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(KeyError)
def missing_param(e):
    return jsonify(error=f'Bad Request - Missing required parameter: {str(e)}'), 400

@app.errorhandler(ValueError)
def invalid_type(e):
    return jsonify(error=str(e)), 400