from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    l_timer.config(text="Timer", fg=GREEN)
    l_ok.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        l_timer.config(fg=RED, text="Long break")
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        l_timer.config(fg=PINK, text="Short break")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        l_timer.config(text="Work")
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            l_ok.config(text="✔")
        else:
            l_ok.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

l_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
l_timer.grid(column=1, row=0)

l_ok = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
l_ok.grid(column=1, row=3)

b_start = Button(text="Start", command=start_timer)
b_start.grid(column=0, row=2)

b_reset = Button(text="Reset", command=reset_time)
b_reset.grid(column=2, row=2)

window.mainloop()
