import tkinter as tk
import random

# Initialize the game variables
player_score = 0
computer_score = 0
games_played = 0

# Function to update the result label
def update_result_label(result):
    result_label.config(text=result)

# Function to update the score labels
def update_scores():
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

# Function to play a single game round
def play(choice):
    global player_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        player_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    update_result_label(result)
    update_scores()

# Function to reset the game for a new round
def new_game():
    global games_played
    games_played += 1
    result_label.config(text="")
    update_scores()

# Function to display the collective score in a pop-up window
def display_collective_score():
    collective_score_window = tk.Toplevel(app)
    collective_score_window.title("Collective Score")
    collective_score_window.geometry("250x100")

    collective_score_label = tk.Label(collective_score_window, text=f"Collective Score: Player {player_score} - Computer {computer_score} (Games Played: {games_played})", font=("Helvetica", 12))
    collective_score_label.pack(pady=10)

# Create the main window
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("400x300")

# Create and configure widgets
frame = tk.Frame(app)
frame.pack(pady=20)

rock_button = tk.Button(frame, text="Rock", width=10, height=2, command=lambda: play("rock"))
paper_button = tk.Button(frame, text="Paper", width=10, height=2, command=lambda: play("paper"))
scissors_button = tk.Button(frame, text="Scissors", width=10, height=2, command=lambda: play("scissors"))

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(frame, text="", font=("Helvetica", 14))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

player_score_label = tk.Label(app, text="Player: 0", font=("Helvetica", 12))
player_score_label.pack()

computer_score_label = tk.Label(app, text="Computer: 0", font=("Helvetica", 12))
computer_score_label.pack()

new_game_button = tk.Button(app, text="New Game", font=("Helvetica", 12), command=new_game)
new_game_button.pack()

quit_button = tk.Button(app, text="Quit and Show Score", font=("Helvetica", 12), command=display_collective_score)
quit_button.pack()

# Start the application main loop
app.mainloop()
