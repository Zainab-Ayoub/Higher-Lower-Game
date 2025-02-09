from art import logo, vs
from gameData import data
import random

print(logo)

def formatData(account):
    accountName = account["name"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    print(f"{accountName}, a {accountDescription}, from {accountCountry}")

def checkAnswer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

accountA = random.choice(data)
accountB = random.choice(data)
if accountA == accountB:
    accountB = random.choice(data)    

print(f"Compare A: {formatData(accountA)}.")    
print(vs)
print(f"Again B: {formatData(accountB)}.")   

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = accountA["follower_count"]
b_follower_count = accountB["follower_count"]