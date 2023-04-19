from flask import Blueprint, request, jsonify, current_app, make_response
import json
from src import db


frank = Blueprint('frank', __name__)

@frank.route('/products', methods = ['POST'])
def add_new_product():
    the_data = request.get_json()
    current_app.logger.info(the_data)

    unitsOnOrder = 0
    beadID = the_data['BeadID']
    productID = the_data['ProductID']
    productName = the_data['ProductName']
    unitsInStock = the_data['UnitsInStock']
    supplierID = the_data.['SupplierID']
    brand = the_data['Brand']
    size = the_data['Size']
    color = the_data['Color']
    material = the_data['Material']
    price = the_data['Price']
    photos = the_data['Photos']
    manufacturingCountry = the_data['ManufacturingCountry']

    query1 = 'insert into BeadProduct (BeadID, ProductName, Material, Price, Color, Size, Brand, ManufacturingCountry, Photos) values ('
    query1 += str(beadID) + "','" 
    query1 += productName + "','" 
    query1 += material + "','" 
    query1 += str(price) + "','" 
    query1 += color + "','"
    query1 += str(size) + "','" 
    query1 += brand + "','"  
    query1 += manufacturingCountry + "','"
    query1 += photos + ')' 

    current_app.logger.info(query1)
    
    query2 = 'insert into Products (ProductID, SupplierID, UnitsOnOrder, UnitsInStock, BeadID) values ('
    query2 += str(productID) + "','"
    query2 += str(supplierID) + "','" 
    query2 += str(unitsOnOrder) + "','"
    query2 += str(unitsInStock) + "','"
    query2 += str(beadID) + ');'
  
    current_app.logger.info(query2)

    return "Success!"


@frank.route('/products/<productID>', methods = ['PUT'])
def handle_update_product(productID):
    unitPrice = request.json['unitPrice']
    unitsInStock = request.json['unitInStock']

    query = 'update Products set UnitPrice = ' + str(unitPrice) + ', UnitsInStock = ' + str(unitsInStock) + ' where ProductID = ' + str(productID) + ';'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


@frank.route('/products/<productID>', methods = ['DELETE'])
def handle_remove_product(productID):
    query = 'delete from Products where ProductID = ' + str(productID) + ';'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


@frank.route('/products/inStock/suppliers/<supplierID>', methods = ['GET'])
def handle_get_in_stock(supplierID):
    query = 'select * from Products where UnitsInStock > 0 and SupplierID = ' + str(supplierID) + ';'
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


@frank.route('/orderDetails/<supplierID>', methods = ['GET'])
def handle_get_supplier_orders(supplierID):
    query = 'select * from OrderDetails join Products where SupplierID = ' + str(supplierID) + ';'
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


@frank.route('/reviews/<productID>', methods = ['GET'])
def handle_get_product_reviews(productID):
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
def handle_new_shipment():
    orderID = request.json['orderID']
    customerID = request.json['customerID']
    orderDate = request.json['orderDate']
    price = request.json['price']

    query = 'insert into Shipments (OrderID, CustomerID, OrderDate, Price)\n'
    query += 'values (' + str(orderID) + ', ' + str(customerID) + ', \'' + str(orderDate) + '\', ' + str(price) + ');'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


@frank.route('/orders/<orderID>', methods = ['DELETE'])
def handle_remove_order(orderID):
    query = 'delete from Orders where OrderID = ' + str(orderID) + ';'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

