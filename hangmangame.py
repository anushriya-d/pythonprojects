import random

words = ("apple", "banana", "orange", "grape", "mango", "peach", "cherry", "melon", "lemon", "berry",
"table", "chair", "window", "door", "floor", "ceiling", "wall", "room", "house", "garden",
"river", "mountain", "forest", "ocean", "desert", "island", "valley", "hill", "lake", "field",
"cat", "dog", "mouse", "horse", "tiger", "lion", "bear", "snake", "eagle", "shark",
"book", "pen", "paper", "notebook", "pencil", "eraser", "marker", "folder", "file", "desk",
"car", "truck", "train", "plane", "boat", "cycle", "bus", "taxi", "scooter", "jeep",
"happy", "sad", "angry", "excited", "tired", "bored", "calm", "brave", "shy", "proud",
"red", "blue", "green", "yellow", "purple", "black", "white", "orange", "pink", "brown",
"sun", "moon", "star", "cloud", "rain", "storm", "wind", "snow", "sky", "light",
"food", "water", "bread", "rice", "milk", "cheese", "fruit", "vegetable", "meat", "soup",

"school", "college", "teacher", "student", "class", "lesson", "exam", "homework", "project", "result",
"music", "song", "dance", "movie", "drama", "art", "paint", "draw", "guitar", "piano",
"phone", "laptop", "tablet", "screen", "keyboard", "mouse", "charger", "battery", "camera", "speaker",
"friend", "family", "mother", "father", "brother", "sister", "uncle", "aunt", "cousin", "child",
"time", "day", "night", "week", "month", "year", "hour", "minute", "second", "clock",
"run", "walk", "jump", "sit", "stand", "sleep", "eat", "drink", "read", "write",
"fast", "slow", "big", "small", "tall", "short", "long", "wide", "narrow", "thick",
"open", "close", "start", "stop", "begin", "end", "enter", "exit", "push", "pull",
"clean", "dirty", "hot", "cold", "warm", "cool", "soft", "hard", "smooth", "rough",
"city", "village", "road", "street", "market", "shop", "store", "mall", "park", "bridge",

"game", "play", "win", "lose", "score", "team", "match", "ball", "goal", "field",
"idea", "plan", "dream", "goal", "task", "work", "job", "career", "skill", "effort",
"truth", "lie", "fact", "story", "news", "voice", "sound", "noise", "signal", "message",
"love", "hate", "care", "help", "share", "give", "take", "keep", "hold", "leave",
"power", "energy", "force", "speed", "weight", "height", "length", "size", "shape", "form")
 
hangman = {0:("    ",
              "    ",
              "    "),
           1:(" o  ",
              "    ",
              "    "),
           2:(" o  ",
              " |  ",
              "    "),
           3:(" o  ",
              "/|  ",
              "    "),
           4:(" o  ",
              "/|\\",
              "    "),
           5:(" o  ",
              "/|\\",
              "/   "),
           6:(" o  ",
              "/|\\",
              "/ \\")}

def display_man(wrong_guesses):
    print("----------------------------")
    for line in hangman[wrong_guesses]:
        print(line)
    print("----------------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:          
            print("Already guessed that!")
            continue

        guessed_letters.add(guess)            
    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            print("Correct!") 
            if "_" not in hint:               
                display_man(wrong_guesses)
                display_hint(hint)
                print("You win!")
                is_running = False
        else:
            wrong_guesses += 1                
            print(f"Wrong! {wrong_guesses}/6")
            if wrong_guesses == 6:           
                display_man(wrong_guesses)
                print(f"Game over! The word was: {answer}")
                is_running = False


if __name__ == "__main__":
    main()