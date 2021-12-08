'''Error Handlers'''

from flask import jsonify
from sqlalchemy.exc import DataError, IntegrityError, ArgumentError, DatabaseError, SQLAlchemyError
from app import app


@app.errorhandler(404)
def resource_not_found(error_msg):
    '''Handler for 404 error'''
    return jsonify(error=str(error_msg)), 404


@app.errorhandler(KeyError)
def key_error(error_msg):
    '''Handler for KeyError'''
    return jsonify(error=f'Bad Request - Missing required parameter: {str(error_msg)}'), 400


@app.errorhandler(ValueError)
def value_error(error_msg):
    '''Handler for ValueError'''
    return jsonify(error=str(error_msg)), 400


@app.errorhandler(DataError)
def data_error(error_msg):
    '''Handler for DataError'''
    return jsonify(error=str(error_msg)), 400


@app.errorhandler(IntegrityError)
def integrity_error(error_msg):
    '''Handler for IntegrityError'''
    return jsonify(error=str(error_msg)), 400


@app.errorhandler(ArgumentError)
def argument_error(error_msg):
    '''Handler for ArgumentError'''
    return jsonify(error=str(error_msg)), 400


@app.errorhandler(DatabaseError)
def database_error(error_msg):
    '''Handler for DatabaseError'''
    return jsonify(error=str(error_msg)), 400


@app.errorhandler(SQLAlchemyError)
def sqlalchemy_error(error_msg):
    '''Handler for SQLAlchemyError'''
    return jsonify(error=str(error_msg)), 400
