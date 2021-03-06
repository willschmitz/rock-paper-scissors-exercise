#game.py

#use os to read env

import random 

import os
from dotenv import load_dotenv
load_dotenv()
x = os.getenv("PLAYER_NAME")


print("Hello! Welcome" ,x, "to Rock, Paper, Scissors, Shoot!")

#Promt User for input 

#x=input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Please choose 'rock' or 'paper' or 'scissors'")
print("--------")
print("User Chose:")
print(user_choice)
print("--------")

# Computer Choice (At Random)

options = ["rock","paper","scissors"]

#Thanks to Gianna Valencia who shared this in our slack
if user_choice not in options:
    print("Not a Valid option")
    exit()

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)
print("--------")

#serena and I worked together to come up with our If statements for determining winner

if user_choice == "rock":
    if computer_choice == "rock":
        print("Its a tie. Want to try again?")
    if computer_choice == "paper":
        print("Oh no. Paper beats Rock. You lost this time.")
    if computer_choice == "scissors":
        print("Congratulations! Rock beats Scissors. You win!")

if user_choice == "paper":
    if computer_choice == "paper":
        print("Its a tie. Want to try again?")
    if computer_choice == "scissors":
        print("Oh no. Scissors beats Paper. You lost this time.")
    if computer_choice == "rock":
        print("Congratulations! Paper beats Rock. You win!")

if user_choice == "scissors":
    if computer_choice == "scissors":
        print("Its a tie. Want to try again?.")
    if computer_choice == "Rock":
        print("Oh no. Rock beats Scissors. You lost this time.")
    if computer_choice == "Paper":
        print("Congratulations! Scissors beats Paper. You win!")

print("--------")

print("Thanks for playing today. Come back soon to play again.")
