#!/usr/bin/env python3
# Write a guessing game. Think of a secret number. Use a while loop to keep asking the user to guess until they get it right.
secret_number = 45
guess = None                
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
print("Congratulations! You've guessed the secret number!")