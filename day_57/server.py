from flask import Flask, render_template
import requests
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html", )

@app.route("/guess/<name>")
def female(name):
    n = name.title()
    url_female = f"https://api.genderize.io?name={name}"
    url_years = f"https://api.agify.io?name={name}"

    fm = requests.get(url_female).json()
    ye = requests.get(url_years).json()
    current_g = fm["gender"]
    current_y = ye["age"]
    return render_template("index.html", y=current_y, g=current_g, nam=n)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
