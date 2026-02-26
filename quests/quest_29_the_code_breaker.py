# Allow a user 3 attempts to guess the secret code (`42`). Give feedback on each guess and stop the game on a correct guess or after 3 failed attempts.
secret_code = 42
attempts = 3                        
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_code:
        print("Congratulations! You've guessed the code!")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")
if attempts == 0:
    print("Game over! You've used all your attempts.")      