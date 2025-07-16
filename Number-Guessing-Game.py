import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 100)
tries = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    tries += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {tries} tries.")
        break
