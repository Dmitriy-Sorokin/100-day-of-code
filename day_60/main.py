from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    log = request.form["username"]
    pas = request.form["password"]
    print(log, pas)
    return render_template("login.html", l=log, p=pas)


if __name__ == "__main__":
    app.run(debug=True)
