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



@mary.route('/yarnProducts/weight/<weight>', methods=[GET])
def filter_by_weight(weight):
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

@mary.route('/yarnProducts/fiber/<fiber>', methods=[GET])
def filter_by_fiber(fiber):
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

@mary.route('/orders/<customerID>', methods=[GET])
def get_past_orders(fiber):
    query = '''
            SELECT *
            FROM orders 
            JOIN orderDetails
            WHERE customerID = customerID
            ORDER BY orderDate DESC
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

@mary.route('/reviews/<productid>', methods=['POST'])
def add_new_review():
    the_data = request.get_json()
    username = the_data['Username']
    photos = the_data['photos']
    rating = the_data['Rating']
    writtenReview = the_data['WrittenReview']
    reviewID = the_data['ReviewID']
    current_app.logger.info(the_data)
    the_query = "insert into projects (username, photos, rating, writtenReview, reviewID)"
    the_query += "values ('" + username + "', '" + photos + "','" + str(rating) + "','" + writtenReview + "','" + reviewID + ")"
    the_data = request.get_json()
    current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

@mary.route('/projects', methods=['GET'])
def get_project():
    cursor = db.get_db().cursor()
    cursor.execute('select * from projects')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@mary.route('/projects', methods=['POST'])
def add_new_project():
    the_data = request.get_json()
    username = the_data['Username']
    hobby = the_data['Hobby']
    hours = the_data['Hours']
    reviewID = the_data['ReviewID']
    photos = the_data['photos']
    productsUsed = the_data['ProductsUsed']
    current_app.logger.info(the_data)
    the_query = "insert into projects (username, hobby, hours, reviewID, photos, productsUsed)"
    the_query += "values ('" + username + "', '" + hobby + "','" + str(hours) + "','" + str(reviewID) + "','" + photos + "','" + str(productsUsed) + ")"
    current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()


@mary.route('/projects/<projectid>', methods=['PUT'])
def update_project(projectid):
    photos = the_data['Photos']
    hours = the_data['Hours']
    productsUsed = the_data['ProductsUsed']
    current_app.logger.info(the_data)
    the_query = "update projects"
    the_query += "set Photos = '" + photos + "', hours = '" + str(hours) + "', ProductsUsed = '" + str(productsUsed) + ")"
    the_query += "where projectid =" + projectid
    current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

@mary.route('/orders/<OrderID>/shipments', methods=['DELETE'])
def delete_order(orderID):
    cursor = db.get_db().cursor()
    cursor.execute('delete from Shipments WHERE OrderID =' + orderID)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response