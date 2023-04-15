from flask import Blueprint, request, jsonify, make_response
import json
from src import db


mary = Blueprint('customers', __name__)

# Get all customers from the DB
@mary.route('/mary', methods=['GET'])
pass

# Get customer detail for customer with particular userID
@mary.route('/mary/<userID>', methods=['GET'])
def get_smthg(userID):
    pass