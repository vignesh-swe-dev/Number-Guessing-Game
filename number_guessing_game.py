"""
Number Guessing Game
Topics practiced: variables, loops, if/else, functions, random module, try/except
"""

import random


def get_guess():
    """Ask the user for a number and handle wrong input."""
    while True:
        try:
            return int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number.")


def play():
    secret = random.randint(1, 100)
    attempts = 0

    print("I picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play()
