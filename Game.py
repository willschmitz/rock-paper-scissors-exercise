#game.py

import random


print("Rock, Paper, Scissors, Shoot!")

#Promt User for input 

#x=input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
print(user_choice)

# Computer Choice (At Random)

options = ["rock","paper","scissors"]

computer_choice = random.choice(options)
print(computer_choice)

