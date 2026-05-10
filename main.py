import tkinter
import  pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# --------------------------- Data --------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

data_to_learn = df.to_dict(orient="records")

# --------------------------- functions --------------------------- #
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_to_learn)
    canvas.itemconfig(card_img, image=card_front_french)
    canvas.itemconfigure(card_title, text="French", fill="Black")
    canvas.itemconfigure(card_word, text=f"{current_card["French"]}", fill="Black")
    timer = window.after(3000, func=change_card)

def change_card():
    canvas.itemconfigure(card_img, image=card_back_english)
    canvas.itemconfigure(card_title, text="English", fill="White")
    canvas.itemconfigure(card_word, text=f"{current_card["English"]}", fill="White")

def remove_word_as_known():
    data_to_learn.remove(current_card)
    new_data_to_learn = pd.DataFrame(data_to_learn)
    new_data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# --------------------------- UI --------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx= 50, pady= 50, background=BACKGROUND_COLOR)

timer = window.after(3000, func=change_card)

canvas = tkinter.Canvas(width= 800, height= 526, background= BACKGROUND_COLOR, highlightthickness= 0)
card_front_french = tkinter.PhotoImage(file="images/card_front.png")
card_back_english = tkinter.PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image= card_front_french)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)
# Buttons
right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness= 0, command=remove_word_as_known)
right_button.grid(column= 1, row= 1)
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image= wrong_img, highlightthickness= 0, command=next_card)
wrong_button.grid(column= 0, row= 1)

next_card()

window.mainloop()