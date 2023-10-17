
import tkinter as tk
import random

def gui_number_guessing_game():
    global secret_number, attempts, name

    def check_guess():
        global attempts
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            feedback_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            feedback_label.config(text="Too high! Try again.")
        else:
            feedback_label.config(text=f"Congratulations, {name}! You guessed the number {secret_number} in {attempts} attempts.")

    def new_game():
        global secret_number, attempts
        secret_number = random.randint(1, 100)
        attempts = 0
        feedback_label.config(text="")
        guess_entry.delete(0, tk.END)

    secret_number = random.randint(1, 100)
    attempts = 0
    name = ""

    window = tk.Tk()
    window.title("Number Guessing Game")

    name_label = tk.Label(window, text="What is your name?")
    name_label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack()

    def start_game():
        global name
        name = name_entry.get()
        instructions_label.config(text=f"I'm thinking of a number between 1 and 100, {name}. Can you guess it?")
        name_label.destroy()
        name_entry.destroy()
        start_button.destroy()

    start_button = tk.Button(window, text="Start", command=start_game)
    start_button.pack()

    instructions_label = tk.Label(window, text="")
    instructions_label.pack()

    guess_entry = tk.Entry(window)
    guess_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=check_guess)
    submit_button.pack()

    feedback_label = tk.Label(window, text="")
    feedback_label.pack()

    new_game_button = tk.Button(window, text="New Game", command=new_game)
    new_game_button.pack()

    window.mainloop()

if __name__ == "__main__":
    gui_number_guessing_game()
