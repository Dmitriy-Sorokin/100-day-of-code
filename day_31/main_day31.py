from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_word_map = {}


try:
    word_map = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/map_transl.csv")
    dict_word_map = original_data.to_dict(orient="records")
else:
    dict_word_map = word_map.to_dict(orient="records")


def generate_english_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_word_map)
    canvas.itemconfig(word_canvas, fill="black", text=current_card["English"])
    canvas.itemconfig(language_canvas, fill="black", text="English")
    canvas.itemconfig(canvas_card, image=font_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(word_canvas, fill="white", text=current_card["Russian"])
    canvas.itemconfig(language_canvas, fill="white", text="Russian")
    canvas.itemconfig(canvas_card, image=back_img)


def is_known():
    dict_word_map.remove(current_card)
    generate_english_word()
    data = pandas.DataFrame(dict_word_map)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
font_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=font_img)
language_canvas = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create button
img_yes = PhotoImage(file="images/right.png")
b_right = Button(image=img_yes, highlightthickness=0, command=is_known)
b_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=img_wrong, highlightthickness=0, command=generate_english_word)
b_wrong.grid(column=0, row=1)

generate_english_word()
window.mainloop()
