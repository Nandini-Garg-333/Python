import random 
words = ["planet", "chocolate", "mountain", "library",
         "elephant", "computer", "painting",
         "festival", "journey", "butterfly"]

word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambledWord = "".join(letters)
print("GAME STARTED!\nYou have only 3 attempts to guess the word...")
print("The Scrambled Word is :",scrambledWord)
attempts = 0 
while attempts<3:
    guess = input("Guess the correct word: ")
    attempts+=1
    if guess == word:
        print("Correct Guess! YOU WIN!")
        print(f"You took {attempts} attempts to guess the word!")
        break
    else:
        print("Incorrect Guess!")
        print(f"You have {3-attempts} attempts left..")
if attempts==3:
    print("YOU LOST!\nThe Correct Word was:",word)