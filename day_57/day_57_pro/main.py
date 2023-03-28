from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:id_b>")
def post(id_b):
    print(type(id_b))
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, num=id_b)

if __name__ == "__main__":
    app.run(debug=True)
