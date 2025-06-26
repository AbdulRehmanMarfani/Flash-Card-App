from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = None 

def next_card_wrong():
    global current_word, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    flash_card.delete("all")
    flash_card.create_image(400, 263, image=flash_card_image)
    flash_card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    flash_card.create_text(400, 263, text=current_word["French"], font=("Ariel", 60, "bold"))
    flip_timer = window.after(3000, flip_card)


def next_card_correct():
    global current_word, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    flash_card.delete("all")
    flash_card.create_image(400, 263, image=flash_card_image)
    flash_card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    flash_card.create_text(400, 263, text=current_word["French"], font=("Ariel", 60, "bold"))
    word_dict.remove(current_word)
    pandas_dataframe = pandas.DataFrame(word_dict)
    pandas_dataframe.to_csv("words_to_learn.csv", index=False)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global flip_timer
    flash_card.delete("all")
    flash_card.create_image(400, 263, image=flash_card_back)
    flash_card.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), fill="white")
    flash_card.create_text(400, 263, text=current_word["English"], font=("Ariel", 60, "bold"), fill="white")
    flip_timer = None

flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_image = PhotoImage(file="card_front.png")
flash_card.grid(row=0, column=0, columnspan=2)
flash_card_back = PhotoImage(file="card_back.png")

wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_card_wrong)
wrong_button.grid(row=1, column=0)

correct_button_image = PhotoImage(file="right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, borderwidth=0, command=next_card_correct)
correct_button.grid(row=1, column=1)
try:
    pandas_dataframe = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    pandas_dataframe = pandas.read_csv("french_words.csv")

word_dict = pandas_dataframe.to_dict(orient="records")

next_card_wrong()

window.mainloop()   