from flask import Flask
from decarat import *
import random

app = Flask(__name__)


@app.route('/')
@h_teg
@img_src
def hello_world():
    return 'Guess a number between 0 and 9'

@app.route("/<int:number>")
@decorator_project_h_l
@h_teg
def greet(number: int):
    random_number = random.randint(1, 10)
    if random_number == number:
        return "You found me!"
    elif number > random_number:
        return "Too high, try again!"
    else:
        return "Too low, try again!"

print(greet(3))
if __name__ == "__main__":
    app.run(debug=True)
