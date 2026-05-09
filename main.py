import tkinter
import  pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
# --------------------------- Data --------------------------- #
df = pd.read_csv("data/french_words.csv")
data = df.to_dict(orient="records")
print(data)
# --------------------------- functions --------------------------- #
def right():
    canvas.itemconfigure(title, text="French")
    canvas.itemconfigure(word, text=f"{data[random.randint(0, len(data) - 1)]["French"]}")

def wrong():
    canvas.itemconfigure(title, text="French")
    canvas.itemconfigure(word, text=f"{data[random.randint(0, len(data) - 1)]["French"]}")


# --------------------------- UI --------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx= 50, pady= 50, background=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width= 800, height= 526, background= BACKGROUND_COLOR, highlightthickness= 0)
card_front =tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image= card_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)
# Buttons
right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness= 0, command=right)
right_button.grid(column= 1, row= 1)
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image= wrong_img, highlightthickness= 0, command=wrong)
wrong_button.grid(column= 0, row= 1)

window.mainloop()