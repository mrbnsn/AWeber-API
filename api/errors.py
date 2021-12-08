from flask import jsonify
from app import app
from sqlalchemy.exc import DataError, IntegrityError, ArgumentError, DatabaseError, SQLAlchemyError


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(KeyError)
def key_error(e):
    return jsonify(error=f'Bad Request - Missing required parameter: {str(e)}'), 400


@app.errorhandler(ValueError)
def value_error(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(DataError)
def data_error(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(IntegrityError)
def integrity_error(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(ArgumentError)
def argument_error(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(DatabaseError)
def database_error(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(SQLAlchemyError)
def sqlalchemy_error(e):
    return jsonify(error=str(e)), 400