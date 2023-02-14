from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Title")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
font_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=font_img)
language_canvas = canvas.create_text(400, 150, text="English", fill="black", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="RANDOM WORD", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create button
img_yes = PhotoImage(file="images/right.png")
b_right = Button(image=img_yes, highlightthickness=0)
b_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=img_wrong, highlightthickness=0)
b_wrong.grid(column=0, row=1)


window.mainloop()
