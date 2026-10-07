# RC, Hangman Homework, CSP 6th

import random

 

 



with open("words.txt", "r") as file:

    words = file.read().splitlines()

 

 



try:

    with open("stats.txt", "r") as file:

        wins = int(file.readline())

        losses = int(file.readline())

except FileNotFoundError:

    wins = 0

    losses = 0

 

 



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

        print("|  {*.*}")

        print("|")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 2:

        print("______")

        print("|    |")

        print("|  {*.*}")

        print("|  [   ]  ")

        print("|")

        print("|_________")

 

    elif wrong_guesses == 3:

        print("______")

        print("|    |")

        print("|  {*.*}")

        print("| /[   ]  ")

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

 

 



def display_word(secret_word, guessed_letters):

    display = ""

 

    for letter in secret_word:

        if letter in guessed_letters:

            display += letter.upper() + " "

        else:

            display += "_ "
    return display
MAX_WRONG_GUESSES = 6
while True:
    secret_word = random.choice(words).lower()
    wrong_guesses = 0
    guessed_letters = []
    print("you won", wins,"times" "  you lost", losses,'times')
    while True:
        print()
        show_hangman(wrong_guesses)
        print("\nWord:", display_word(secret_word, guessed_letters))
        if guessed_letters:
            print('guesses', ", ".join(guessed_letters).upper())
        else:
            print("guesses")
        print("Wrong guesses remaining:", MAX_WRONG_GUESSES - wrong_guesses)

        guess = input("tell me a letter ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():

            print("Please enter one letter.")

            continue

        if guess in guessed_letters:

            print("You already guessed that letter.")

            continue

        guessed_letters.append(guess)

        if guess in secret_word:

            print("Nice!", guess.upper(), "is corect")

 

        else:

            print( guess, "is incorect")

            wrong_guesses += 1

 

        

        word_complete = True

 

        for letter in secret_word:

            if letter not in guessed_letters:

                word_complete = False

 

        if word_complete:

            print("\nyou guessed", secret_word)

            wins += 1

            break

 

        

        if wrong_guesses == MAX_WRONG_GUESSES:

            show_hangman(wrong_guesses)

            print("\nhaha loser")

            print("The word was:", secret_word)

            losses += 1

            break

 

 

    

    with open("stats.txt", "w") as file:
        file.write(str(wins) + "\n")
        file.write(str(losses) + "\n")

    print("\nUpdated Stats — Wins:", wins, "Losses:", losses)
    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()


    if play_again != "yes":
        print("well to darn bad")
        break