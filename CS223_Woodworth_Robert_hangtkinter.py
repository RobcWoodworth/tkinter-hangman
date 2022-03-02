#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import random
tk = Tk()
tk.title("Hangman game")
tk['background'] = '#ffa82e'
tk.geometry("800x500")
my_words = ["THROWN", "THROWN", "THROWN", "THROWN", "THROWN", "THROWN",
            "THROWN", "THROWN", "THROWN", "THROWN", "THROWN", "THROWN"]
hung = ["T", "T", "T", "T", "T", "T", "T", "T", "T"]
answer, wrongs, wins, life = my_words[random.randint(0, 11)], [], 0, 8
lbl_word = Label(tk, text="--  " * 6, font=("Arial", 65), bg="#ffa82e")
lbl_word.place(x=155, y=55)
lbl_man = Label(tk, text="T", font=("Arial", 90), bg="#ffa82e")
lbl_man.place(x=220, y=200)
lbl_wron = Label(tk, text=f"Bad guesses: {wrongs}", font=("Arial", 15),
                 bg="#ffa82e")
lbl_wron.place(x=320, y=420)
field = Entry(tk, justify=CENTER, font=("Arial", 55))
field.place(x=20, y=400, width=90)
display, the_word = ["--", "--", "--", "--", "--", "--"], "--  " * 6


def hangman():
    global life, wins, lbl_wron, lbl_word
    global wrongs, answer, hung, the_word, display, my_words, wins
    letter = field.get()[0].capitalize()
    if letter.isalpha() is False:
        messagebox.showwarning("Hey", "That's not a letter")
        field.delete(0, END)
        return
    if letter in answer:
        if letter in display:
            messagebox.showwarning("Hey", "Already guessed that")
            field.delete(0, END)
        else:
            display[answer.find(letter)] = letter    # Search for letter in-
            wins += 1          # -answer then replace display index with letter
            field.delete(0, END)
            the_word = "  ".join(display)
            lbl_word["text"] = f"{the_word}"
    else:
        life -= 1
        wrongs.append(letter), field.delete(0, END)
        lbl_man["text"] = f"{hung[8-life]}"
        lbl_wron["text"] = f"Bad guesses: {wrongs}"
        messagebox.showerror("Oops", f"{letter} is not in word!!")
    if wins >= 6:
        the_word = "  ".join(display)
        lbl_word["text"] = f"{the_word}"
        messagebox.showinfo("Congrats!", "Winner")
        reset()
    if life <= 0:
        lbl_man["text"] = f"{hung[8-life]}"
        messagebox.showerror("Oh No", "Dead")
        reset()


def reset():
    global my_words, answer, display, the_word, lbl_wron, wrongs, life, wins
    global lbl_man
    field.delete(0, END)
    display = ["--", "--", "--", "--", "--", "--"]
    the_word = "--  " * 6
    lbl_man["text"] = "T"
    wins = 0
    life = 8
    lbl_word['text'], lbl_wron["text"] = "--  " * 6, "Bad guesses: []"
    answer = my_words[random.randint(0, 20)]


Button(tk, width=9, text="Submit", font=("Arial", 25),
       command=hangman, bg="#af7").place(x=130, y=410)
Button(tk, width=9, text="Reset", command=reset).place(x=15, y=80)
Button(tk, width=4, text="Exit", font=("Arial", 20),
       command=quit, fg='#fff', bg="#f00").place(x=10, y=10)
tk.mainloop()
