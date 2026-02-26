# Quest 25: The Number Wizard
# A guessing game that tells the user if their guess is too high or too low

secret_number = 42

print("I am the Number Wizard. I'm thinking of a number between 1 and 100.")

guess = int(input("Enter your guess: "))

while guess != secret_number:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Enter your guess: "))

print("You got it! The number was 42. The wizard bows in defeat.")
