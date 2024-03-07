import random


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

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 2:
    print('You win!')