from vending.db import db


class Machine(db.Model):
    __tablename__ = "Machine"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100))

    def __init__(self, code, address):
        self.code = code
        self.address = address
