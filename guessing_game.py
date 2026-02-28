"""Simple number guessing game.

The program randomly selects a number between 1 and 10 and asks the user to guess it.
It gives feedback on whether the guess is too high or too low until the correct number is guessed.
"""

import random


def play_game():
    number = random.randint(1, 10)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_game()
