# import a random library to help with generating computer choices.
import random

# initial scores.
user_wins = 0
computer_wins = 0

# the valid options for this game.
options = ["rock", "paper", "scissors"]

# While loop to keep asking the user for a choice.
while True:
 # asking the user for input >> converting it to lowercase.
    user_input = input("Please enter (rock/paper/scissors) or Q to quit:\n").lower()
    # Generate a number randomly from 0 to 2.
    computer_random = random.randint(0,2)
    # assign a choice for the computer based on the random number from 0 to 2 from the options list.
    computer_choice = options[computer_random]
# check if the user input is q to quit the app.
    if user_input == "q":
        print("see you soon","your score is",user_wins,"and the PC is",computer_wins)
        break
# check if user input is not valid.
    elif user_input not in options:
        print("please Enter a valid choice!")
        continue
# check both user and computer inputs.
    elif user_input == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("computer choose ",computer_choice)
        print("you won!, ","your score is",user_wins,"and the PC is",computer_wins )
    elif user_input == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("computer choose ", computer_choice)
        print("you won!, ", "your score is", user_wins, "and the PC is", computer_wins)
    elif user_input == "paper" and computer_choice == "rock":
        user_wins += 1
        print("computer choose ", computer_choice)
        print("you won!, ", "your score is", user_wins, "and the PC is", computer_wins)
    elif user_input == computer_choice:
        print("It is the same choice,try again!")
    else:
        computer_wins += 1
        print("computer choose ", computer_choice)
        print("you lost!, ", "your score is", user_wins, "and the PC is", computer_wins)
