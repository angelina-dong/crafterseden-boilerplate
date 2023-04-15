from flask import Blueprint, request, jsonify, make_response
import json
from src import db


mary = Blueprint('mary', __name__)

# Get all customers from the DB
@mary.route('/products/<productID>', methods=['GET'])
def get_product_details(productID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from products where productid = {0}'.format(productID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    


# Get customer detail for customer with particular userID
@mary.route('/mary/<userID>', methods=['GET'])
def get_smthg(userID):
    pass
pass

@mary.route('/mary/yarnProducts/weight/<weight>', methods=[GET])
def filter_by_weight(weight)
    query = '''
            SELECT *
            FROM yarnProducts
            WHERE yarnProducts.weight = weight
            ORDER BY name ASC
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]
    
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@mary.route('/mary/yarnProducts/fiber/<fiber>', methods=[GET])
def filter_by_weight(weight)
    query = '''
            SELECT *
            FROM yarnProducts
            WHERE yarnProducts.fiber = fiber
            ORDER BY name ASC
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]
    
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)