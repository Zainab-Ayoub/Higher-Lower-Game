from art import logo, vs
from gameData import data
import os 
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
score = 0
gameShouldContinue = True
accountB = random.choice(data)

def formatData(account):
    accountName = account["name"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescription}, from {accountCountry}"

def checkAnswer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"
while gameShouldContinue:
    accountA = accountB
    accountB = random.choice(data)
    
    while accountA == accountB:
        accountB = random.choice(data)    

    print(f"Compare A: {formatData(accountA)}.")    
    print(vs)
    print(f"Against B: {formatData(accountB)}.")   

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = accountA["follower_count"]
    b_follower_count = accountB["follower_count"]
    isCorrect = checkAnswer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)

    if isCorrect:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")  
        gameShouldContinue = False  