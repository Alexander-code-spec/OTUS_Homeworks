import os
from flask import Flask
from flask_migrate import Migrate
from werkzeug.exceptions import InternalServerError
from models import db
from views.users import users_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))

app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def root():
    return "<h1>Hello World!</h1>"


@app.errorhandler(KeyError)
def handle_key_error(exc):
    return InternalServerError(f"could not find that by key {exc}!")


@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(exc):
    print("exc", exc)
    return InternalServerError("could divide that!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
