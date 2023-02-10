from tkinter import *

window = Tk()
window.title("Miles to kilometer Converter")
window.minsize(height=150, width=300)

entry = Entry()
entry.grid(column=1, row=0)

l_miles = Label(text="Miles")
l_miles.grid(column=2, row=0)
l_miles.config(pady=20)

l_equal = Label(text="is equal to")
l_equal.grid(column=0, row=1)
l_equal.config(padx=20)

l_num_km = Label(text="0")
l_num_km.grid(column=1, row=1)
l_num_km.config(pady=10)

l_km = Label(text='Km')
l_km.grid(column=2, row=1)


def calculate():
    mil = entry.get()
    km = int(mil) * 1.609
    l_num_km.config(text=int(km))


b_calculate = Button(text="Calculate", command=calculate)
b_calculate.grid(column=1, row=2)

window.mainloop()
