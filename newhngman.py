# RC, Hangman Homework, CSP 6th

import random

 

# Get words from words.txt

with open("words.txt", "r") as file:

    words = file.read().splitlines()

 

# Get wins and losses from stats.txt

try:

    with open("stats.txt", "r") as file:

        wins = int(file.readline())

        losses = int(file.readline())

except FileNotFoundError:

    wins = 0

    losses = 0

 

# Show the hangman

def show_hangman(wrong):

    pictures = [

        "______\n|    |\n|\n|\n|\n|_________",

        "______\n|    |\n|    O\n|\n|\n|_________",

        "______\n|    |\n|    O\n|    |\n|\n|_________",

        "______\n|    |\n|    O\n|   /|\n|\n|_________",

        "______\n|    |\n|    O\n|   /|\\\n|\n|_________",

        "______\n|    |\n|    O\n|   /|\\\n|   /\n|_________",

        "______\n|    |\n|    O\n|   /|\\\n|   / \\\n|_________"

    ]

    print(pictures[wrong])

 

# Show the word with blanks

def show_word(word, guessed):

    result = ""

    for letter in word:

        if letter in guessed:

            result += letter.upper() + " "

        else:

            result += "_ "

    return result

 

# 6 wrong guesses are allowed

MAX_WRONG = 6

 

while True:

    word = random.choice(words).lower()

    guessed = []

    wrong = 0

 

    while True:

        show_hangman(wrong)

        print("\nWord:", show_word(word, guessed))

        print("Guessed:", ", ".join(guessed).upper())

        print("Wrong guesses remaining:", MAX_WRONG - wrong)

 

        guess = input("Guess a letter: ").lower()

 

        if len(guess) != 1 or not guess.isalpha():

            print("Please enter one letter.")

            continue

 

        if guess in guessed:

            print("You already guessed that letter!")

            continue

 

        guessed.append(guess)

 

        if guess in word:

            print("Nice!", guess.upper(), "is in the word!")

        else:

            print("Sorry,", guess.upper(), "is not in the word!")

            wrong += 1

 

        # Check for a win

        if all(letter in guessed for letter in word):

            print("\nCongratulations! You guessed", word.upper())

            wins += 1

            break

 

        # Check for a loss

        if wrong == MAX_WRONG:

            show_hangman(wrong)

            print("\nYou lost! The word was", word.upper())

            losses += 1

            break

 

    # Save stats

    with open("stats.txt", "w") as file:

        file.write(str(wins) + "\n")

        file.write(str(losses))

 

    print("\nAll-Time Stats")

    print("Wins:", wins)

    print("Losses:", losses)

 

    again = input("\nPlay again? (yes/no): ").lower()

 

    if again != "yes":

        print("Thanks for playing!")

        break