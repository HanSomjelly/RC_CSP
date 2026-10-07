# RC, Hangman, CSP 6th
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
    # i made my hangman a cute robot :)
def hangman(wrong):
    if wrong == 0:
        print("______")
        print("|    |")
        print("|")
        print("|")
        print("|")
        print("|_______-")
    elif wrong == 1:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("|")
        print("|")
        print("|_________")
    elif wrong == 2:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("|  [   ]")
        print("|")
        print("|________")
    elif wrong == 3:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("| /[   ]")
        print("|")
        print("|________")
    elif wrong == 4:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("| /[   ]\\")
        print("|")
        print("|_______")
    elif wrong == 5:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("| /[   ]\\")
        print("|  _|")
        print("|_________")
    elif wrong == 6:
        print("______")
        print("|    |")
        print("|  {*.*}")
        print("| /[   ]\\")
        print("|  _| |_")
        print("|_________")
def show_word(word, guessed):
    result = ""
    for letter in word:
        if letter in guessed:
            result += letter.upper() + " "
        else:
            result += "_ "
    return result
MAX_WRONG = 6
while True:
    word = random.choice(words).lower()
    guessed = []
    wrong = 0
    while True:
        hangman(wrong)
        print()
        print("word so far", show_word(word, guessed))
        if guessed:
            print("you guessed", ", ".join(guessed).upper())
        else:
            print("you guessed")
        print("you have this many wrong guesses left", MAX_WRONG - wrong)
        guess = input("tell me a letter")
        if len(guess) != 1 or not guess.isalpha():
            print("only one LETTER (has to be a letter)")
            continue
        if guess in guessed:
            print("brutha, you already said that")
            continue
        guessed.append(guess)
        if guess in word:
            print(guess.upper(), "is one of them")
        else:
            print(guess.upper(), "isnt in the word")
            wrong += 1
        if all(letter in guessed for letter in word):
            print("good job yiu guessed", word.upper())
            wins += 1
            break
        if wrong == MAX_WRONG:
            hangman(wrong)
            print("haha loser the word was", word)
            losses += 1
            break
    with open("stats.txt", "w") as file:
        file.write(str(wins))
        file.write("\n")
        file.write(str(losses))
    print()
    print("Wins:", wins)
    print("Losses:", losses)
    again = input("do you want to play hangman again? plese only say YES or NO ").lower()
    if again != "yes":
        print("hashtag Sad_soLonely")
        break