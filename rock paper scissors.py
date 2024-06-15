import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Please enter (rock/paper/scissors) or Q to quit:\n").lower()
    computer_random = random.randint(0,2)
    computer_choice = options[computer_random]

    if user_input == "q":
        print("see you soon","your score is",user_wins,"and the PC is",computer_wins)
        break

    elif user_input not in options:
        print("please Enter a valid choice!")
        continue

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
