from tkinter import *

window = Tk()
window.title("KM to Miles Converter")
window.minsize(500, 300)
window.config(padx=35, pady=35)

# input
km = Entry(width=7)
km.grid(column=2, row=1)

# Label
km_label = Label(text="KM", font=("Arial", 16, "normal"))
km_label.grid(column=3, row=1)

convert_label = Label(text="is equal to", font=("Arial", 16, "normal"))
convert_label.grid(column=1, row=2)

mi_count = Label(text="0", font=("Arial", 16, "normal"))
mi_count.grid(column=2, row=2)

mi_label = Label(text="Miles", font=("Arial", 16, "normal"))
mi_label.grid(column=3, row=2)


def km_to_mi():
    kilometers = float(km.get())
    miles = round(kilometers * 0.621371, 2)
    mi_count.config(text=miles)


# Button
calculate = Button(text="Calculate", command=km_to_mi)
calculate.grid(column=2, row=3)

window.mainloop()
