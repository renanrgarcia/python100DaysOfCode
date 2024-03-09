import random
import os


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

restart = 'y'
while restart == 'y':
    os.system('cls')
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    gallery = [rock, paper, scissors]

    if player_choice >= 3 or player_choice < 0:
        print('You typed an invalid number.')
    else:
        print(gallery[player_choice])
        
        print('Computer choice:')
        print(gallery[computer_choice])

        if player_choice == 0 and computer_choice == 2:
            print('You win!')
        elif player_choice > computer_choice: 
            print('You win!')
        elif player_choice == 2 and computer_choice == 0:
            print('You lose!')
        elif player_choice < computer_choice:
            print('You lose!')
        elif player_choice == computer_choice:
            print('It\'s a draw!')


    restart = input('Do you want to play again? ("y" or "n") ').lower()