from flask import Blueprint, request, jsonify, current_app, make_response
import json
from src import db


frank = Blueprint('frank', __name__)

@frank.route('/products', methods = ['POST'])
def handle_new_product():
    name = request.json['name']
    unitsOnOrder = 0
    unitsInStock = request.json['unitsInStock']
    # dateAdded = request.json['dateAdded']
    supplierID = request.json['supplierID']
    name = request.json['name']
    brand = request.json['brand']
    size = request.json['size']
    color = request.json['color']
    material = request.json['material']
    unitPrice = request.json['unitPrice']
    photos = request.json['photos']
    manufacturingCountry = request.json['manufacturingCountry']

    query = 'insert into BeadProduct (Brand, Size, Color, Material, UnitPrice, Photos, ManufacturingCountry, Name)\n'
    query += 'values (\'' + str(brand) + '\', ' + str(size) + ', \'' + str(color) + '\', \'' + str(material) + '\', '
    query += str(unitPrice) + ', \'' + str(photos) + '\', \'' + str(manufacturingCountry) + '\', \'' + str(name) + '\');'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    query = 'select BeadID from BeadProduct where name = ' + name + ';'

    cursor.execute(query)
    db.get_db().commit()
    the_data = cursor.fetchall()
    beadID = 0
    for row in the_data:
        beadID = row[0]
    
    query = 'insert into Products (SupplierID, UnitsOnOrder, UnitsInStock, DateAdded, BeadID)\n'
    query += 'values (\'' + str(supplierID) + '\', ' + str(unitsOnOrder) + ', ' + str(unitsInStock) + ', ' + str(beadID) + ');'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
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

