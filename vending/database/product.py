from datetime import datetime

from vending.db import db


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    machine_id = db.Column(db.String(100), db.ForeignKey("Machine.code"))
    product_id = db.Column(db.String(100), unique=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    name = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer, unique=True)
    price = db.Column(db.Float, unique=True)

    def __init__(self, machine_id, product_id, name, quantity, price) -> None:
        self.machine_id = machine_id
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
