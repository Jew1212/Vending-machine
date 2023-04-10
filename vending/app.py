from flask import Flask

from vending.api.machine_route import machine_controller
from vending.api.product_route import product_controller
from vending.db import db


def create_app() -> Flask:
    """High level support for doing this and that."""
    application: Flask = Flask(__name__)

    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test12.sqlite"
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(application)
    with application.app_context():
        db.create_all()

    application.register_blueprint(machine_controller)
    application.register_blueprint(product_controller)
    return application


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
