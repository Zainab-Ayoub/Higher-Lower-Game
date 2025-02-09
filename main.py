from art import logo, vs
from gameData import data
import random

print(logo)

def formatData(account):
    accountName = account["name"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    print(f"{accountName}, a {accountDescription}, from {accountCountry}")

accountA = random.choice(data)
accountB = random.choice(data)
if accountA == accountB:
    accountB = random.choice(data)    

print(f"Compare A: {formatData(accountA)}.")    
print(f"Compare B: {formatData(accountB)}.")    