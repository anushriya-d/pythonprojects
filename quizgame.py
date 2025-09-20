# Quiz Game Program

quess = ("What is the capital of Canada?" , 
        "Which planet is known as the 'Red Planet'?",
        "Who was the first President of the United States?",
        "What is the national animal of India?")

options = (("A. Ottawa" , "B. Jaipur ", "C. NYC", "D. Paris"),
           ("A. Earth" , "B. Mercury", "C. Mars", "D. Saturn"),
           ("A. Barack Obama" , "B. George Washington", "C. Ronald Reagan", "D. Franklin D. Roosevelt"),
           ("A. Bengal Tiger" , "B. Dolphin", "C. Cheetah", "D. Elephant"))

anss = ("A","C","B","A")
guesses = []
score = 0
num = 0

for ques in quess:
    print("-----------------------------------------------------------------------------------")
    print(ques)

    for option in options [num]:
        print(option)


    guess=input("Enter your guess(A, B, C, D):").upper()
    guesses.append(guess)
    if guess == anss[num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{anss[num]} is the correct answer.")
    num+=1

print("---------------------------------------------------------------------------------")
print("                                 RESULTS                                         ")
print("---------------------------------------------------------------------------------")

print("answers:  ", end=" ")
for ans in anss:
    print(ans, end=" ")
print()

print("guessses:  ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(quess) * 100)
print(f"Your score is: {score}%")