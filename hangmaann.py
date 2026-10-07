# RC, Hangman Homework, CSP 6th

import random

 

 

# Read the list of possible words from words.txt

with open("words.txt", "r") as file:

    words = file.read().splitlines()

 

 

# Read the win/loss totals from stats.txt

try:

    with open("stats.txt", "r") as file:

        wins = int(file.readline())

        losses = int(file.readline())

except FileNotFoundError:

    wins = 0

    losses = 0

 

 

# Function to display the hangman

def show_hangman(wrong_guesses):

    if wrong_guesses == 0:

        print("______")

        print("|    |")

        print("|")

        print("|")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 1:

        print("______")

        print("|    |")

        print("|    O")

        print("|")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 2:

        print("______")

        print("|    |")

        print("|    O")

        print("|    |")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 3:

        print("______")

        print("|    |")

        print("|    O")

        print("|   /|")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 4:

        print("______")

        print("|    |")

        print("|    O")

        print("|   /|\\")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 5:

        print("______")

        print("|    |")

        print("|    O")

        print("|   /|\\")

        print("|   /")

        print("|_________")

 

    elif wrong_guesses == 6:

        print("______")

        print("|    |")

        print("|    O")

        print("|   /|\\")

        print("|   / \\")

        print("|_________")

 

 

# Function to display the guessed letters and blanks

def display_word(secret_word, guessed_letters):

    display = ""

 

    for letter in secret_word:

        if letter in guessed_letters:

            display += letter.upper() + " "

        else:

            display += "_ "

 

    return display

 

 

# 6 wrong guesses are allowed

MAX_WRONG_GUESSES = 6

 

 

# Main game loop

while True:

 

    # Pick a random word

    secret_word = random.choice(words).lower()

 

    # Reset the game

    wrong_guesses = 0

    guessed_letters = []

 

    print("\nLoading word list from words.txt...")

    print("Loading stats from stats.txt...")

    print("Wins:", wins, "Losses:", losses)

 

    # Hangman game loop

    while True:

 

        print()

        show_hangman(wrong_guesses)

 

        print("\nWord:", display_word(secret_word, guessed_letters))

 

        if guessed_letters:

            print("Guessed letters:", ", ".join(guessed_letters).upper())

        else:

            print("Guessed letters: (none yet)")

 

        print("Wrong guesses remaining:", MAX_WRONG_GUESSES - wrong_guesses)

 

        # Ask the player for a letter

        guess = input("Guess a letter: ").lower().strip()

 

        # Make sure the player entered one letter

        if len(guess) != 1 or not guess.isalpha():

            print("Please enter one letter.")

            continue

 

        # Check for repeated guesses

        if guess in guessed_letters:

            print("You already guessed that letter.")

            continue

 

        # Add the guess to the guessed letters

        guessed_letters.append(guess)

 

        # Check if the letter is in the word

        if guess in secret_word:

            print("Nice!", guess.upper(), "is in the word!")

 

        else:

            print("Sorry,", guess.upper(), "is not in the word.")

            wrong_guesses += 1

 

        # Check if the player won

        word_complete = True

 

        for letter in secret_word:

            if letter not in guessed_letters:

                word_complete = False

 

        if word_complete:

            print("\nCongratulations! You guessed the word:", secret_word.upper())

            wins += 1

            break

 

        # Check if the player lost

        if wrong_guesses == MAX_WRONG_GUESSES:

            show_hangman(wrong_guesses)

            print("\nYou lost!")

            print("The word was:", secret_word.upper())

            losses += 1

            break

 

 

    # Save the updated statistics

    with open("stats.txt", "w") as file:

        file.write(str(wins) + "\n")

        file.write(str(losses) + "\n")

 

    # Display all-time statistics

    print("\nUpdated Stats — Wins:", wins, "Losses:", losses)

 

    # Ask if the player wants another game

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

 

    if play_again != "yes":

        print("Thanks for playing Hangman!")

        break