import random
from tkinter import *

# Console version of the game
def main():
    number_to_guess = random.randint(1, 100)
    attempts_remaining = 10
    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100.")
    
    while attempts_remaining > 0:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Congratulations! You guessed it!")
            break
        
        attempts_remaining -= 1
        print(f"Attempts remaining: {attempts_remaining}")
    
    else:
        print(f"Sorry! The number was {number_to_guess}.")

# GUI version of the game
def start_game():
    global number_to_guess, attempts_remaining
    number_to_guess = random.randint(1, 100)
    attempts_remaining = 10
    hint_label.config(text="Guess a number between 1 and 100")
    attempts_label.config(text=f"Attempts remaining: {attempts_remaining}")

def check_guess():
    global attempts_remaining
    try:
        guess = int(entry.get())
        if guess < number_to_guess:
            hint_label.config(text="Too Low!")
        elif guess > number_to_guess:
            hint_label.config(text="Too High!")
        else:
            hint_label.config(text="Congratulations! You guessed it!")
            return
        
        attempts_remaining -= 1
        attempts_label.config(text=f"Attempts remaining: {attempts_remaining}")
        
        if attempts_remaining == 0:
            hint_label.config(text=f"Sorry! The number was {number_to_guess}.")
    
    except ValueError:
        hint_label.config(text="Please enter a valid integer.")

# Uncomment this line to run the console version
# main()

# GUI setup
root = Tk()
root.title("Guess the Number")

hint_label = Label(root, text="")
hint_label.pack()

entry = Entry(root)
entry.pack()

submit_button = Button(root, text="Submit Guess", command=check_guess)
submit_button.pack()

attempts_label = Label(root, text="")
attempts_label.pack()

start_game() # Initialize game on startup

root.mainloop()