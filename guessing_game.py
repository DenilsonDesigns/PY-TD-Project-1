"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    # intro message
    print("Welcome to PyGuess")
    print("==================")
    # generate a random num 1-10
    answer = random.randint(1, 10)
    # generate variable to hold num of guesses
    num_guesses = 0
    # boolean to break loop
    guessed_correct = False
    # continuously prompt player to guess until correct

    while guessed_correct == False:
        try:
            print("Guess a number between 1 and 10")
            guess = input()
            guess = int(guess)
        except ValueError:
            print("Please enter only integers between 1 and 10 (inclusive)")
            continue
        if guess > 10 or guess < 1:
            print("Please choose a number between 1 and 10 (inclusive)")
            continue
        num_guesses += 1
        if guess < answer:
            print("It's higher")
        elif guess > answer:
            print("It's lower")
        if guess == answer:
            print("You guessed correct! It took you {} tries!".format(num_guesses))
            print("Exiting game: Thanks for playing! :)")
            guessed_correct = True

    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
