from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
LANGUAGE_FRONT = "French"
LANGUAGE_BACK = "English"
current_card = {}
new_words = {}

try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    origin_words = pandas.read_csv("./data/french_words.csv")
    new_words = origin_words.to_dict(orient="records")
else:
    new_words = words.to_dict(orient="records")


# Select words
def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(new_words)
    canvas.itemconfig(card, image=card_img)
    canvas.itemconfig(language, fill="black", text=LANGUAGE_FRONT)
    canvas.itemconfig(word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card, image=back_card_img)
    canvas.itemconfig(language, fill="white", text=LANGUAGE_BACK)
    canvas.itemconfig(word, fill="white", text=current_card["English"])


def known_words():
    new_words.remove(current_card)
    data = pandas.DataFrame(new_words)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_word()


# Create the UI
window = Tk()
window.title("Flashcards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Flashcard Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(405, 272, image=card_img)
language = canvas.create_text(400, 150, text="", fill="black", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=(FONT, 60, "bold"))
canvas.grid(column=1, columnspan=2, row=1)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_word)
wrong_button.grid(column=1, row=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_words)
right_button.grid(column=2, row=2)

new_word()

window.mainloop()
