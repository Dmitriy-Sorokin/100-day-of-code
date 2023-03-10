from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(4, 6))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(4, 6))]

    random.shuffle(password_list)

    password = "".join(password_list)

    e_password.delete(0, END)
    e_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    get_web = e_website.get().lower()
    get_pass = e_password.get()
    get_email = e_email.get()
    new_data = {
        get_web: {
            "email": get_email,
            "password": get_pass,
        }
    }

    if len(get_pass) <= 0 or len(get_web) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=get_web, message=f"These are the details entered: \nEmail: {get_email}"
                                                              f"\nPassword: {get_pass} \nIs it ok to save")

        if is_ok:
            try:
                with open("data.json", mode="r") as data:
                    # Reading old data
                    r_data = json.load(data)
                    # Update old data
                    r_data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", mode="w") as data:
                    # Saving update data
                    json.dump(r_data, data, indent=4)
            finally:
                # json.dump(new_data, data, indent=4)
                # r_data = json.load(data)
                e_website.delete(0, END)
                e_password.delete(0, END)


# ---------------------------- Function search ------------------------------- #

def find_password():
    get_web = e_website.get().lower()
    try:
        with open("data.json", mode="r") as data:
            read_data = json.load(data)
            messagebox.showinfo(title=get_web,
                                message=f"Your email: {read_data[get_web]['email']}\n"
                                        f"Your password: {read_data[get_web]['password']}")
            e_website.delete(0, END)
    except KeyError:
        messagebox.showwarning(title="Warning", message=f"No details for {get_web} exists.")
        e_website.delete(0, END)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Create canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create label
l_website = Label(text="Website:")
l_website.grid(column=0, row=1)

l_email_username = Label(text="Email/Username:")
l_email_username.grid(column=0, row=2)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3)

# Create entry

e_website = Entry(width=34)
e_website.grid(column=1, row=1)
e_website.focus()

e_email = Entry(width=52)
e_email.insert(END, "bashkavit1992@gmail.com")
e_email.grid(column=1, row=2, columnspan=2)

e_password = Entry(width=34)
e_password.grid(column=1, row=3)

# Create button

b_generate_pass = Button(text="Generate Password", width=14, command=generate_password)
b_generate_pass.grid(column=2, row=3)

b_add = Button(text="Add", width=44, command=save_password)
b_add.grid(column=1, row=4, columnspan=2)

b_search = Button(text="Search", width=14, command=find_password)
b_search.grid(column=2, row=1)

window.mainloop()
