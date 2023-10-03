# import tkinter
from tkinter import *

window = Tk()  # Creates the window
window.title("Summer is cool")
window.minsize(500, 300)  # Default window size
window.config(padx=30, pady=30)

# Labels
my_label = Label(text="Label", font=("Arial", 24, "bold"))  # Create a label
my_label.grid(column=1, row=1)  # Places item on screen
my_label.config(text="New Label")  # Update properties of label


# Buttons

def button_clicked():
    my_label.config(text=user_input.get())
    print("Your mom")


button = Button(text="Click Here", command=button_clicked)
# button.place(x=150, y=50)
# button.pack() Grid a pack cannot be used together
button.grid(column=2, row=2)

new_button = Button(text="New Button")
new_button.grid(column=3, row=1)

# Entry Component

user_input = Entry(width=12)
user_input.grid(column=4, row=3)

window.mainloop()  # Keeps the window on screen
