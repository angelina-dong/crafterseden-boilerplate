from flask import Blueprint, request, jsonify, make_response
import json
from src import db


mary = Blueprint('customers', __name__)

# Get all customers from the DB
@mary.route('/mary', methods=['GET'])
pass

# Get customer detail for customer with particular userID
@mary.route('/mary/<userID>', methods=['GET'])
<<<<<<< HEAD
def get_smthg(userID):
    pass
=======
pass

@mary.route('/mary/yarnProducts/weight/{weight}')
pass
>>>>>>> e0aa61eb15808b89fbd0863fd412d2e8d31813cb
