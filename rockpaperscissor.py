import random

options= ( "rock", "scissors", "paper")
running = True

while running:

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
    
    play_again = input("Play again (y/n) : ").lower()      #if input("Play again (y/n) : ").lower() == "n":
    if play_again == "n":                                  #        running=False
        running= False                                     
        print("Hope you enjoy the game!")
