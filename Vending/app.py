from flask import Flask
from Vending.api.machine_route import machine_controller
from Vending.api.product_route import product_controller
from Vending.db import db


def create_app():
    application: Flask = Flask(__name__)

    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test5.sqlite'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(application)
    with application.app_context():
        db.create_all()

    application.register_blueprint(machine_controller)
    application.register_blueprint(product_controller)
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
