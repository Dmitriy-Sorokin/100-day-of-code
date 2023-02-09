import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=600, height=400)

# Label
my_label = tkinter.Label(text="I am label", font=("Arial", 24, "bold"))
my_label.pack()


window.mainloop()
