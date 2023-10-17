Created my 1st Algorithm: Number Guessing Game using Python. 
Firstly, what is an 
A
 lgorithm
 ?
 Well, it’s like a recipe or a set of instructions that tells a computer, or even a person, how to 
do a specific task.  
It's a step-by-step plan that helps you solve a problem or perform a task in an organized and 
logical way.  
Think of it as a clear and precise set of directions to achieve a desired outcome. 
For example, if you're making a sandwich, you follow a simple algorithm: 
1) 
Take two slices of bread. 
2) 
Spread some peanut butter on one slice. 
3) 
Spread some salted butter on the other slice. 
4) 
Press the two slices of bread together. 
5) 
Cut the sandwich in half. 
In this above example, the algorithm guides you through the process of making a sandwich.  
Algorithms are used in all kinds of areas, not just in cooking.  
They are essential in computer programming, maths, and various fields to solve problems 
and complete tasks efficiently and accurately. 
Basically, the computer will randomly select a number, and the player will have to guess it. 
The computer will provide hints to help the player find the correct number. 
So here is my 1st EVER Algorithm: Number Guessing Game using Python and 
the steps involved. 
Step 1: Define the Problem 
The computer selects a random number between a specified range (e.g., 1 to 100). 
The player tries to guess the number. 
The computer provides feedback if the guess is too high, too low, or correct. 
Repeat until the player guesses the correct number.  
Step 2:
 Pseudocode
 ( Pseudocode is like a rough draft of a program) 
Step 3: Implementation (in Python) 
You NEED to download a code editor like VS code or PyCharm as that’s where you will write 
your code.  
What is a code editor?  A code editor is a specialized software tool for writing and 
editing code, offering features like syntax highlighting, auto-completion, and error checking 
to make coding easier and more efficient.  
It's essential for software development and helps programmers write and manage code 
effectively. 
You can THEN implement this algorithm in Python as follows. *See below*  
Step 4: Play the Game Run the Python code, and you'll have a simple and fun number 
guessing game. Try to guess the randomly selected number within the specified range.  
import random 
 
def number_guessing_game(): 
    # Define the range of numbers to guess from 
    low_range = 1 
    high_range = 100 
 
    # Generate a random number within the range 
    secret_number = random.randint(low_range, high_range) 
 
    # Keep track of the number of attempts 
    attempts = 0 
 
    # Prompt for player's name 
    name = input("What is your name? ") 
 
    # Greet the player 
    print(f"Hello, {name}! Welcome to the Number Guessing Game!") 
    print(f"I'm thinking of a number between {low_range} and {high_range}.") 
 
    # Loop until the player guesses the correct number 
    while True: 
        # Get the player's guess 
        try: 
            guess = int(input("Enter your guess: ")) 
        except ValueError: 
            print("Invalid input! Please enter a valid integer.") 
continue 
# Increment the number of attempts 
attempts += 1 
# Check if the guess is too low, too high, or correct 
if guess < secret_number: 
print("Too low! Try again.") 
elif guess > secret_number: 
print("Too high! Try again.") 
else: 
print(f"Congratulations, {name}! You guessed the number {secret_number} in 
{attempts} attempts.") 
break 
if __name__ == "__main__": 
number_guessing_game() 
