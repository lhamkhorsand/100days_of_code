import sys
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
#


placeholder = (len(chosen_word)) * ['-']

lives = 6
display = placeholder
checked_letters = []

while '-' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in checked_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    checked_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    print("Word so far: ", ' '.join(display))
    print("Guessed letters: ", ' '.join(checked_letters))
    print(stages[lives])

if '-' not in display:
    print("YOU WIN!!! ")
else:
    print(" GAME OVER!!! The word was:", chosen_word)
