from flask import Flask
from decarat import *

app = Flask(__name__)


@app.route('/')
@h_teg
@u_teg
@img_src
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)
