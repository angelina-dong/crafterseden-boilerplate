from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


mary = Blueprint('mary', __name__)

@mary.route('/products/<productID>', methods=['GET'])
def get_product_details(productID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Products where ProductID = ' + str(productID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@mary.route('/yarnProduct/weight/<weight>', methods=['GET'])
def filter_by_weight(weight):
    query = 'SELECT * FROM YarnProduct WHERE YarnWeight = ' + str(weight) +' ORDER BY ProductName ASC'
    
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

@mary.route('/yarnProduct/fiber/<fiber>', methods=['GET'])
def filter_by_fiber(fiber):
    query = 'SELECT * FROM YarnProduct WHERE Fiber = ' + str(fiber) + ' ORDER BY ProductName ASC'
    
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

@mary.route('/orders/<customerID>', methods=['GET'])
def get_past_orders(customerID):
    query = 'SELECT * FROM Orders JOIN OrderDetails WHERE CustomerID = ' + str(customerID) + ' ORDER BY OrderDate DESC'
    
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

@mary.route('/reviews', methods=['POST'])
def add_new_review():
    the_data = request.get_json()
    current_app.logger.info(the_data)

    username = the_data['Username']
    photos = the_data['Photos']
    rating = the_data['Rating']
    productID = the_data['ProductID']
    writtenReview = the_data['WrittenReview']

    the_query = f''' 
            INSERT INTO Reviews(Username, Photos, Rating, WrittenReview, ProductID)
            VALUES ('{username}', '{photos}', '{rating}', '{writtenReview}', '{productID}')
        '''
   
    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()
 
    return "Success!"

@mary.route('/projects', methods=['GET'])
def get_project():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Projects')
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
    current_app.logger.info(the_data)

    # projectid = the_data['ProjectID']
    username = the_data['Username']
    productsUsed = the_data['ProductsUsed']
    hobby = the_data['Hobby']
    hours = the_data['Hours']
    reviewID = the_data['ReviewID']
    photos = the_data['Photos']
    

    the_query = f''' 
            INSERT INTO Projects(Username, Hobby, Hours, ReviewID, Photos, ProductsUsed)
            VALUES ('{username}', '{hobby}', '{hours}', '{reviewID}', '{photos}', '{productsUsed}')
        '''

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"


@mary.route('/projects/<projectid>', methods=['PUT'])
def update_project(projectid):
    the_data = request.get_json()
    current_app.logger.info(the_data)

    photos = the_data['Photos']
    hours = the_data['Hours']
    productsUsed = the_data['ProductsUsed']

    the_query = f''' 
            update Projects
            set Hours = '{hours}', Photos = '{photos}', ProductsUsed = '{productsUsed}'
            where ProjectID = '{projectid}';
        '''
   
    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

@mary.route('/orders/<OrderID>', methods=['DELETE'])
def delete_order(OrderID):
    query = 'delete from Orders WHERE OrderID = ' + str(OrderID) + ';'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"
