from flask import Blueprint, request, jsonify, current_app, make_response
import json
from src import db


frank = Blueprint('frank', __name__)


@frank.route('/mostExpensive') # change this /mostExpensive
    pass

@frank.route('/categories', methods = ['GET'])
    pass


@frank.route('/frank', methods=['POST'])
    pass

@frank.route('/tenMostExpensive', methods=['GET'])
    pass

@frank.route('/frank', method = ['POST'])
    pass