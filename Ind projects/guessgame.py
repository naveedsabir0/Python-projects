import random

num = random.randint(1, 9)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 9: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
    elif guess>num:
        print("High")
    elif guess<num:
        print("low")
    else:
        print("nope, sorry. try again!")