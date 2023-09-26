from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(choice(letters))

    password_list = [choice(letters) for char in range(nr_letters)]
    password_list += [choice(symbols) for char in range(nr_symbols)]
    password_list += [choice(numbers) for char in range(nr_numbers)]
    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        empty = messagebox.showinfo(title="Error", message="Please do not leave any fields empty!")
    else:
        add_entry = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \n Email: {email} \nPassword: {password}\nSave?")

        if add_entry:
            with open("data.txt", "a") as passwords:
                passwords.write(f"Website: {website}; Email: {email}; Password: {password}\n")
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Website Entry
website_label = Label(text="Website: ", font=(FONT_NAME, 12, "normal"))
website_label.grid(column=1, row=2)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, columnspan=2, row=2)

# Email & Username Entry
email_label = Label(text="Email/Username: ", font=(FONT_NAME, 12, "normal"))
email_label.grid(column=1, row=3)

email_entry = Entry(width=35)
email_entry.insert(0, "summer.hamilton@hey.com")
email_entry.grid(column=2, columnspan=2, row=3)

# Generate Password
pass_label = Label(text="Password: ", font=(FONT_NAME, 12, "normal"))
pass_label.grid(column=1, row=4)

pass_entry = Entry(width=21)
pass_entry.grid(column=2, row=4)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=3, row=4)

# Add to db
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=2, columnspan=2, row=5)

window.mainloop()
