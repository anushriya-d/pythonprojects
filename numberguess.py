import random

lowest= 1
highest= 100
ans= random.randint(lowest, highest)
guesses = 0
is_running = True

print("----------Python Number Guessing Game----------")
print(f"Guess the number between {lowest} to {highest}.")

while is_running:
    guess= input("Enter your guess : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("The number is out of range.")
            print(f"Please select the number between {lowest} to {highest}.")
        elif guess< ans:
            print("Too low! Try again!")
        elif guess> ans:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {ans}.")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest} and {highest}.")