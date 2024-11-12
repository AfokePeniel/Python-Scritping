"""
This is a very common game and despite its underlying complexity, 
the game’s rules are straightforward. 
Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.

This is achieved while a player enters a choice and python randomly chooses using the random module.

"""

#Rock Papper Scissors Game

import random

print("Welcome to Rock,Papper,Scissors Game!!!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer = ["rock", "paper", "scissors"]
choice_computer = random.choice(computer)

player = input('Choose and Enter any hand signal between "rock", "paper", "scissors": ')

if player == "rock" and choice_computer == "scissors":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose rock ")
    print(rock)
    print("While Computer chose scissors")
    print(scissors)
    print("Rock wins against scissors!, Congrats Player!")
    print(rock)
elif choice_computer == "rock" and player == "scissors":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose scissors ")
    print(scissors)
    print("While Computer chose rock")
    print(rock)
    print("Rock wins against scissors!, Congrats Computer!")
    print(rock)  
elif player == "scissors" and choice_computer == "paper":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose scissors ")
    print(scissors)
    print("While Computer chose paper")
    print(paper)
    print("Scissors wins against Paper!, Congrats Player!")
    print(scissors) 
elif player == "paper" and choice_computer == "scissors":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose paper ")
    print(paper)
    print("While Computer chose scissors")
    print(scissors)
    print("Scissors wins against Paper!, Congrats Computer!")
    print(scissors) 
elif player == "paper" and choice_computer == "rock":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose paper ")
    print(paper)
    print("While Computer chose rock")
    print(rock)
    print("Paper wins against Rock!, Congrats Player!")
    print(paper) 
elif player == "rock" and choice_computer == "paper":
    print("Rock Paper Scissors Shoot!!!...")
    print("You as a Player chose rock ")
    print(rock)
    print("While Computer chose paper")
    print(paper)
    print("Paper wins against Rock!, Congrats Computer!")
    print(paper) 
    
elif player == choice_computer:
    print("It's a draw!")
else:
    print("Wrong choice. Please choose within the given option, Thanks")
     