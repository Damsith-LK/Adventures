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

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f'Psst, the solutioon is {chosen_word}.')
display = []

for _ in range(word_length):
    display += '_'

while not end_of_game:
    good = False
    guess = input('Guess a number: ').lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            lives = lives
            good = True

    if not good:
        lives -= 1

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You win.')
    elif lives == 0:
        print('You lose.')
        end_of_game = True


print(stages[lives])