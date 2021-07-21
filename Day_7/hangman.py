import random

# Global Variables
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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
WORD_LIST = ["aardvark", "baboon", "camel"]
RANDOM_WORD = random.choice(WORD_LIST)
WORD_LENGTH = len(RANDOM_WORD)
print(RANDOM_WORD)
DISPLAY = []
SEPERATOR = " "
LETTER_BANK = []
LIVES = 6
END_OF_GAME = False


# Sets the display for word
for _ in range(WORD_LENGTH):
    DISPLAY += "_"

# Game Setup
while not END_OF_GAME:
    print(stages[LIVES])
    print(f"You have {LIVES} lives...")
    print(SEPERATOR.join(DISPLAY))
    print(f"Guessed Letters: {LETTER_BANK}")
    GUESS = input("Guess a letter: ").lower()
    
    if GUESS in LETTER_BANK:
        print("Sorry you've chosen this letter before.")
    else:
        GUESSED_LETTERS = LETTER_BANK.append(GUESS)

    for i in range(WORD_LENGTH):
        letter = RANDOM_WORD[i]
        if letter == GUESS:
            DISPLAY[i] = letter
    

    if GUESS not in RANDOM_WORD:
        LIVES -= 1
    
    if "_" not in DISPLAY:
        END_OF_GAME = True
        print(f"You win! The word is {''.join(DISPLAY)}. Thanks for playing!")
    elif LIVES == 0:
        print("Sorry, you loose...")
        END_OF_GAME = True
    
