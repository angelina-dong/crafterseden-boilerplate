from flask import Blueprint, request, jsonify, current_app, make_response
import json
from src import db


frank = Blueprint('frank', __name__)

@frank.route('/products', methods = ['POST'])

def add_new_product():
    the_data = request.get_json()
    current_app.logger.info(the_data)
    
    productName = the_data['ProductName']
    brand = the_data['Brand']
    size = the_data['Size']
    color = the_data['Color']
    material = the_data['Material']
    price = the_data['Price']
    photos = the_data['Photos_A']
    manufacturingCountry = the_data['ManufacturingCountry']

    # beadID = the_data['BeadID']
    unitsOnOrder = 0
    unitsInStock = the_data['UnitsInStock']
    supplierID = the_data['SupplierID']

    query1 = f''' 
            INSERT INTO BeadProduct(ProductName, Material, Price, Color, Size, Brand, ManufacturingCountry, Photos)
            VALUES ('{productName}', '{material}', '{price}', '{color}', '{size}', '{brand}', '{manufacturingCountry}', '{photos}');
        '''

    current_app.logger.info(query1)

    cursor = db.get_db().cursor()
    cursor.execute(query1)
    db.get_db().commit()

    query2 = f'''select BeadID from BeadProduct where ProductName = '{productName}';
    '''

    cursor.execute(query2)
    db.get_db().commit()
    the_data = cursor.fetchall()

    beadID = 0
    for row in the_data:
        beadID = row[0]

    query3 = f''' 
            INSERT INTO Products(BeadID, UnitsInStock, SupplierID, UnitsOnOrder)
            VALUES ('{beadID}', '{unitsInStock}', '{supplierID}', '{unitsOnOrder}');
        '''
  
    current_app.logger.info(query3)

    cursor.execute(query3)
    db.get_db().commit()

    return "Success!"

@frank.route('/products/<productID>', methods = ['PUT'])
def update_product(productID):

    the_data = request.get_json()
    current_app.logger.info(the_data)

    unitsInStock = the_data['UnitsInStock_U']

    the_query = f''' 
            update Products
            set UnitsInStock = '{unitsInStock}'
            where ProductID = '{productID}';
        '''
    
    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

@frank.route('/products/<productID>', methods = ['DELETE'])
def remove_product(productID):

    the_query = 'delete from Products where ProductID = ' + str(productID) + ';'
    
    current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "Success!"

@frank.route('/products/inStock/suppliers/<supplierID>', methods = ['GET'])
def get_in_stock(supplierID):
    cursor = db.get_db().cursor()
    query = 'select * from Products where UnitsInStock > 0 and SupplierID = ' + str(supplierID) + ';'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@frank.route('/orderDetails/<supplierID>', methods = ['GET'])
def get_orders(supplierID):
    cursor = db.get_db().cursor()
    query = 'select * from OrderDetails join Products where SupplierID = ' + str(supplierID) + ';'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@frank.route('/reviews/<productID>', methods = ['GET'])
def get_reviews(productID):
    query = 'select * from Reviews where ProductID = ' + str(productID) + ' ;'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@frank.route('/shipments', methods = ['POST'])
def create_shipment():
    the_data = request.get_json()
    current_app.logger.info(the_data)

    orderID = the_data['OrderID']
    shippingAddress = the_data['ShippingAddress']
    carrier = the_data['Carrier']
    trackingID = the_data['TrackingID']

    the_query = f''' 
            INSERT INTO Shipments(OrderID, ShippingAddress, Carrier, TrackingID)
            VALUES ('{orderID}', '{shippingAddress}', '{carrier}', '{trackingID}')
        '''

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()
    return "Success!"


@frank.route('/orders/<orderID>', methods = ['DELETE'])
def remove_order(orderID):
    query = 'delete from Orders where OrderID = ' + str(orderID) + ';'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return "Success!"

