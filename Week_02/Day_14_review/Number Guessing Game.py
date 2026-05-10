# Number Guessing Game

import random

secret = random.randint(1, 10)
attempts = 3

print("--- Number Guessing Game (1 to 10) ---")

while attempts > 0:
    print(f"\nAttempts remaining: {attempts}")
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Winner! ")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
        attempts -= 1  

if attempts == 0:
    print(f"\nBetter luck next time! Answer was: {secret}")