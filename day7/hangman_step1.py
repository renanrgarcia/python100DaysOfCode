# Step 1

from random import choice


word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. # noqaE501
word = choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. # noqaE501
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. # noqaE501
for letter in word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

