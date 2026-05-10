import random

secret = random.randint(1, 10)
attempts = 3

print("--- Number Guessing Game (1 to 10) ---")
print("Type '0' to exit the game anytime.")

while attempts > 0:
    print(f"\nAttempts remaining: {attempts}")
    user_input = input("Guess the number: ")

    
    if user_input == '0':
        print("Exiting game... Goodbye!")
        break
    guess = int(user_input)
    attempts -= 1  

    if guess == secret:
        print("Winner! ")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

if attempts == 0 and guess != secret:
    print(f"\nBetter luck next time! Answer was: {secret}")