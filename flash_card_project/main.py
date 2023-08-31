import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    to_learn = pd.read_csv("data/words_to_learn.csv").to_dict(orient='records')
except FileNotFoundError:
    to_learn = pd.read_csv("data/french_words.csv").to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
check_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas.grid(row=0, column=0, columnspan=2)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))

known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()