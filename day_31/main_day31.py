from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Serialization file CSV

word_map = pandas.read_csv("data/map_transl.csv")
dict_word_map = word_map.to_dict(orient="records")

# print(dict_word_map[random_num]["English"])

# print(dict_word_map["Russian"])
new_english_word = []


def generate_english_word():
    random_eng_word = random.choice(dict_word_map)["English"]
    random_ru_word = random.choice(dict_word_map)["Russian"]
    canvas.itemconfig(word_canvas, text=random_eng_word)
    canvas.itemconfig(language_canvas, text="English")
    # time.sleep(3)
    # canvas.itemconfig(language_canvas, fill="blue", text="Russian")
    # canvas.create_image(400, 263, image=back_img)
    back


# Create canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
font_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
font = canvas.create_image(400, 263, image=back_img)
back = canvas.create_image(400, 263, image=font_img)
language_canvas = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create button
img_yes = PhotoImage(file="images/right.png")
b_right = Button(image=img_yes, highlightthickness=0, command=generate_english_word)
b_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=img_wrong, highlightthickness=0, command=generate_english_word)
b_wrong.grid(column=0, row=1)

generate_english_word()
window.mainloop()
