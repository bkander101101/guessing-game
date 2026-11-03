from analyticskit import *
import random

while True:
    # Generate a random number
    secret_number = random.randint(1, 10)

    # Ask the user to guess
    guess = single_input("Guess a number between 1 and 10.")

    # Check the guess
    if guess == str(secret_number):
        show_message("You Win!", "You win! You guessed the correct number.")
    else:
        show_message("You Lose!", f"You lose. The correct number was {secret_number}.")

    # Ask whether the user wants to play again
    play_again = single_input("Would you like to play again? Enter y/n.")

    if play_again.lower() != 'y':
        break