import tkinter as tk
import random
from tkinter import messagebox

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)

    result = ""
    if choice == computer:
        result = "It's a draw!"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Scissors" and computer == "Paper") or \
         (choice == "Paper" and computer == "Rock"):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"You: {choice} | Computer: {computer}\n{result}")

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

title = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 12))
title.pack(pady=10)

btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=5)

root.mainloop()