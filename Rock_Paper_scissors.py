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
images = [rock, paper, scissors]

computer_choice = random.randint(0,2)
player_choice = int(input('what number do you choose? 0, 1 or 2\n'))

while player_choice>2 or player_choice<0:
    player_choice = int(input('invalid number. please enter again 0, 1 or 2\n'))


print(f'you:\n {images[player_choice]}')
print(f'computer:\n {images[computer_choice]}')

if player_choice == computer_choice:
    print('It\'s a draw!')
elif player_choice == 0 and computer_choice ==2:
    print('you win')
elif player_choice == 2 and computer_choice == 0:
    print('you lost')
elif player_choice > computer_choice:
    print('you win')
elif player_choice < computer_choice:
    print('you lose')


