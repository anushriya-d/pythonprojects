import random

options= ( "rock", "scissors", "paper")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

print(f"Player : {player}")
print(f"Computer : {computer}")

if player == computer:
    print("Sorry! It's a Tie.")
# wins you will have
elif player == "rock" and computer == "scissors":
    print("YAHOOOOO! You Win 🥳")
elif player == "scissors" and computer == "paper":
    print("YAHOOOOO! You Win 🥳")  
elif player == "paper" and computer == "rock":
    print("YAHOOOOO! You Win 🥳") 
else:
    print("OOPSSS! You Lose 😢")