import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x300")
        self.root.config(bg="#FFCC00")

        self.choices = ["rock", "paper", "scissors"]

        self.label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="#FFCC00")
        self.label.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 15), bg="#FFCC00")
        self.result_label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", font=("Arial", 15), command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.paper_button = tk.Button(root, text="Paper", font=("Arial", 15), command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.scissors_button = tk.Button(root, text="Scissors", font=("Arial", 15), command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.result_label.config(text=f"You chose {player_choice}. Computer chose {computer_choice}. {result}")

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a Draw!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "You Win!"
        else:
            return "Computer Wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
