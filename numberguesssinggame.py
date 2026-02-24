import random
def RandomNumGuess(targetNum):
    attempts = 0
    while True:
        guess = int(input("Guess a Number Between 1-100 : "))
        attempts+=1
        if guess==targetNum:
            print("Number guessed!\nThe Attempts taken are:",attempts)
            return
        elif guess>targetNum:
            print("Too High!")
        elif guess<targetNum:
            print("Too Low!") 
print("Game Started!")
targetNum = random.randint(1,100)
RandomNumGuess(targetNum)