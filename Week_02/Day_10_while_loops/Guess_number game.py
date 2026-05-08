secret = 7
while True:
    guess = int(input("Guess: "))
    if guess == secret:
        print("Correct! ")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")