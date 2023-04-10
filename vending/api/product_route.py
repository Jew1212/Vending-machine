from flask import Blueprint, jsonify, request

from vending.database.product import Product
from vending.manager import Manager

product_controller = Blueprint("product_controller", __name__)


@product_controller.route("/addProduct/", methods=["POST"])
def add_product():
    """High level support for doing this and that."""
    machine_id = request.json["machine_id"]
    product_id = request.json["product_id"]
    name = request.json["name"]
    quantity = request.json["quantity"]
    price = request.json["price"]
    manager = Manager()
    machine = manager.find_machine(code=machine_id)
    if machine:
        manager.add_product(machine_id, product_id, name, quantity, price)
        return request.json
    else:
        return jsonify(message="Unidentified Machine Identity", status=404)


@product_controller.route("/everyProduct/", methods=["GET"])
def all_product():
    """High level support for doing this and that."""
    producters = Product.query.all()
    product_list = [
        {
            "id": i.id,
            "machine_id": i.machine_id,
            "product_id": i.product_id,
            "time": i.time,
            "name": i.name,
            "quantity": i.quantity,
            "price": i.price,
        }
        for i in producters
    ]
    return jsonify(product_list)


@product_controller.route("/deleteProduct/", methods=["DELETE"])
def delete_product():
    """High level support for doing this and that."""
    product_id = request.json["product_id"]
    manager = Manager()
    product = manager.find_product(product_id=product_id)
    if product:
        manager.delete_product(product_id)
        return request.json
    else:
        return jsonify(message="Unidentify Stock Identity", status=404)


@product_controller.route("/editProduct/", methods=["PUT"])
def edit_product():
    """High level support for doing this and that."""
    product_id = request.json["product_id"]
    manager = Manager()
    product = manager.find_product(product_id=product_id)
    if product:
        name = request.json["name"]
        quantity = request.json["quantity"]
        price = request.json["price"]
        manager.edit_product(product_id, name, quantity, price)
        return request.json
    else:
        return jsonify(message="Unidentify Stock Identity", status=404)
