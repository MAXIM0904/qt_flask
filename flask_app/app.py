from flask import Flask, g

from flask_app.api.v1.data_processing import processing
from flask_app.create_db import create_sqlite

app = Flask(__name__)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


app.register_blueprint(processing, url_prefix="/v1")


@app.route("/")
def hello():
    return "Hello, World!"


def main():
    create_sqlite()
    app.run(host='127.0.0.1', port=5000)


if __name__ == "__main__":
    main()
