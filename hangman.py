# RC, Hangman
import random
import os

# CReate a list of possible words on a seperate txt file
with.open("hangman.txt", "r") as file:
    txtfile = file.readlines()


scrtword = random.coice


# create another file  holds win/loss counts

# use split(",") on the content of the words txt document to create your list of words

# pull win and lose totals from the other txt file and save them as 2 nseperate variables

# build hangman game

# save  the correct word as a variable  random.choice(name of the list)
# number of wrong guesses
# what letters have been guessed


# function to display the hangman (needs number of wrong guesses)
"""______
   |     |
   |     O
   |    /|\\
   |    / \\
   |_________
   """



# function that has to show the letters and spaces (the correct word, letters that have been guessed)
# loop the correct word
    # variable for display word
    # check if letter has been guessed
        # then add letter to the display word
    # if they have not guessed the lettter
        # add an underscore to the display word
    # return the finished display word (outside of the loop)

    # main game loop (while true)
    # call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add letter to the list of guessed letters
    # check if letter is in word:
        # increase incorrect guesses
    #check if display word is same as the word
      # tell user they won
     # increase win total
     # ask if they want to play again
           # reset random word, rest wrong guess count
       # check to see if they loss (they have 6 wrong guesses)
            #tell them they lost
            # tell them what the word was
            # incresae the lost count
            # ask if they want to play again
                        #reset random word, rest wrong guess count 