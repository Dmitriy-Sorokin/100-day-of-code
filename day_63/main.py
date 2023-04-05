from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    fin = ""
    for dict_books in all_books:
        for items in dict_books:
            fin += dict_books[items] + "/10" + "<br>"

    return render_template("index.html", f=fin)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        # NOTE: You can use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)

