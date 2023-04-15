from flask import Blueprint, request, jsonify, current_app, make_response
import json
from src import db


frank = Blueprint('frank', __name__)

@frank.route('/products', method = ['POST'])
def handle_new_product():
    name = request.json['name']
    units_on_order = request.json['units_on_order']
    units_in_stock = request.json['units_in_stock']
    date_added = request.json['date_added']
    supplier_id = request.json['supplier_id']
    name = request.json['name']
    brand = request.json['brand']
    size = request.json['size']
    color = request.json['color']
    material = request.json['material']
    unit_price = request.json['unit_price']
    photos = request.json['photos']
    manufacturing_country = request.json['manufacturing_country']

    query = 'insert into BeadProduct (Brand, Size, Color, Material, UnitPrice, Photos, ManufacturingCountry, Name)\n'
    query += 'values (\'' + brand + '\', ' + str(size) + ', \'' + color + '\', \'' + material + '\', '
    query += str(unit_price) + ', \'' + photos + '\', \'' + manufacturing_country + '\', \'' + name + '\');'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()

    query = 'select BeadID from BeadProduct where name = ' + name + ';'

    cursor.exectue(query)
    db.get_db().commit()
    the_data = cursor.fetchall()
    bead_id = 0
    for row in the_data:
        bead_id = row[0]
    
    query = 'insert into Product (SupplierID, UnitsOnOrder, UnitsInStock, DateAdded, BeadID)\n'
    query += 'values (\'' + supplier_id + '\', ' + str(units_on_order) + ', ' + str(units_in_stock) + ', ' + str(date_added) + ', ' + str(bead_id) + ');'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()


@frank.route('/products/<productID>', method = ['PUT'])
def handle_update_product(product_id):
    unit_price = request.json['unit_price']
    units_in_stock = request.json['units_in_stock']

    query = 'update Products set UnitPrice = ' + str(unit_price) + ', UnitsInStock = ' + str(units_in_stock) + ' where ProductID = ' + str(product_id) + ';'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()


@frank.route('/products/<productID>', method = ['DELETE'])
def handle_remove_product(product_id):
    query = 'delete from Products where ProductID = ' + str(product_id) + ';'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()


@frank.route('/products/inStock', method = ['GET'])
def handle_get_in_stock():
    query = 'select * from Products where UnitsInStock > 0;'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
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


@frank.route('/orderDetails/<supplierID>', method = ['GET'])
def handle_get_supplier_orders(supplier_id):
    query = 'select * from OrderDetails join Products where SupplierID = ' + str(supplier_id) + ';'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
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


@frank.route('/reviews/<product_id>', method = ['GET'])
def handle_get_product_reviews(product_id):
    query = 'select * from Reviews where ProductID = ' + str(product_id) + ';'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
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


@frank.route('/shipments', method = ['POST'])
def handle_new_shipment():
    order_id = request.json['order_id']
    customer_id = request.json['customer_id']
    order_date = request.json['order_date']
    price = request.json['price']

    query = 'insert into Shipments (OrderID, CustomerID, OrderDate, Price)\n'
    query += 'values (' + str(order_id) + ', ' + str(customer_id) + ', \'' + order_date + '\', ' + str(price) + ');'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()


@frank.route('/orders/<orderID>', method = ['DELETE'])
def handle_remove_order(order_id):
    query = 'delete from Orders where OrderID = ' + str(order_id) + ';'
    cursor = db.get_db().cursor()
    cursor.exectue(query)
    db.get_db().commit()

