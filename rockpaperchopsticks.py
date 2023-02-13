# Symbols: 🪨, 📄, 🥢

import time
import random

decidingInt = random.randint(1,3) # Randomising numbers that represent either rock, paper or chopsticks
if decidingInt == 1:
    randomChoice = "Rock 🪨"
elif decidingInt == 2:
    randomChoice = "Paper 📄"
else:
    randomChoice = "Chopsticks 🥢"

print("Lets play rock paper chopsticks!")
rockPaperOrChopsticks = input("(R)ock, (P)aper or (C)hopsticks? ") # Getting user's choice
if rockPaperOrChopsticks.lower() == "r": # Allows you type lowercase and uppercase
    humanChoice = "Rock 🪨"
    print("You choose", humanChoice)
elif rockPaperOrChopsticks.lower() == "p":
    humanChoice = "Paper 📄"
    print("You choose", humanChoice)
elif rockPaperOrChopsticks.lower() == "c":
    humanChoice = "Chopsticks 🥢"
    print("You choose", humanChoice)
else:
    print("Type either R, P or C")
    exit()
    
x = 4
while x > 1: # Countdown 
    x -= 1
    print(str(x) + "...")
    time.sleep(1)
    if x == 1:
        print("Computer's choice is:", randomChoice) # Random choice
    else:
        continue

if randomChoice == humanChoice: # Deciding who wins
    print("It's a draw!")
elif humanChoice == "Rock 🪨" and randomChoice == "Chopsticks 🥢":
    print("You win!")
elif humanChoice == "Paper 🥢" and randomChoice == "Chopsticks 📄":
    print("You win!")
elif humanChoice == "Chopsticks 📄" and randomChoice == "Rock 🪨":
    print("You win")
else:
    print("You lose!")






