"""
# project 1

import random

while True:
    choice = input("Roll the dice? (y/n): ") .lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thank for playing!")
        break
    else:
        print("Invalid choice!")

"""

"""
# Project 2

import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
             print("Congratulation! You guessed the number.")
             break
    except ValueError:
        print("Please enter a valid number")


"""
